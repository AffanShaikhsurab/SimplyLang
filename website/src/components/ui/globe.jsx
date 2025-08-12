import React, { useRef, useEffect } from 'react';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import { useTheme } from '../../contexts/ThemeContext';

const Globe = () => {
    const mountRef = useRef(null);
    const { theme } = useTheme();

    useEffect(() => {
        const currentMount = mountRef.current;
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, currentMount.clientWidth / currentMount.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(currentMount.clientWidth, currentMount.clientHeight);
        currentMount.appendChild(renderer.domElement);

        const isDarkMode = theme === 'dark';

        const topColor = isDarkMode ? "#2d3748" : "#ffffff";
        const bottomColor = isDarkMode ? "#1a202c" : "#ffe1f0";
        const dotColor = isDarkMode ? 0xa0aec0 : 0x4d4d4d;
        const orangeDotColor = isDarkMode ? 0xed8936 : 0xff753d;

        const geometry = new THREE.SphereGeometry(5, 64, 32, 0, Math.PI);
        const material = new THREE.ShaderMaterial({
            uniforms: {
                topColor: { value: new THREE.Color(topColor) },
                bottomColor: { value: new THREE.Color(bottomColor) },
            },
            vertexShader: `
                varying vec3 vNormal;
                void main() {
                    vNormal = normal;
                    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
                }
            `,
            fragmentShader: `
                uniform vec3 topColor;
                uniform vec3 bottomColor;
                varying vec3 vNormal;
                void main() {
                    float mixValue = vNormal.y * 0.5 + 0.5;
                    vec3 color = mix(bottomColor, topColor, mixValue);
                    gl_FragColor = vec4(color, 1.0);
                }
            `,
        });

        const globe = new THREE.Mesh(geometry, material);
        scene.add(globe);

        const dotGeometry = new THREE.BufferGeometry();
        const numDots = 2000;
        const positions = new Float32Array(numDots * 3);
        for (let i = 0; i < numDots * 3; i += 3) {
            const phi = Math.acos(-1 + (2 * Math.random()));
            const theta = Math.random() * Math.PI * 2;
            const radius = 5;
            if (phi < Math.PI) {
                positions[i] = radius * Math.sin(phi) * Math.cos(theta);
                positions[i + 1] = radius * Math.cos(phi);
                positions[i + 2] = radius * Math.sin(phi) * Math.sin(theta);
            }
        }
        dotGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        const dotMaterial = new THREE.PointsMaterial({
            color: dotColor,
            size: 0.05,
            transparent: true,
        });
        const dots = new THREE.Points(dotGeometry, dotMaterial);
        scene.add(dots);

        const createOrangeDot = (lat, lon) => {
            const radius = 5.01;
            const phi = (90 - lat) * Math.PI / 180;
            const theta = (lon + 180) * Math.PI / 180;
            const x = radius * Math.sin(phi) * Math.cos(theta);
            const y = radius * Math.cos(phi);
            const z = radius * Math.sin(phi) * Math.sin(theta);
            const dotGeometry = new THREE.SphereGeometry(0.1, 16, 8);
            const dotMaterial = new THREE.MeshBasicMaterial({ color: orangeDotColor });
            const dot = new THREE.Mesh(dotGeometry, dotMaterial);
            dot.position.set(x, y, z);
            globe.add(dot);
        };

        createOrangeDot(40.7, -74);
        createOrangeDot(34, -118);

        camera.position.z = 10;
        camera.position.y = 1;

        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.rotateSpeed = 0.5;

        const animate = () => {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        };

        animate();

        const handleResize = () => {
            camera.aspect = currentMount.clientWidth / currentMount.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(currentMount.clientWidth, currentMount.clientHeight);
        };

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
            currentMount.removeChild(renderer.domElement);
        };
    }, [theme]);

    return <div ref={mountRef} style={{ width: '100%', height: '500px' }} />;
};

export default Globe;