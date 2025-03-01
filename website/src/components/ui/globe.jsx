import React, { useRef, useEffect } from 'react';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

const Globe = () => {
    const mountRef = useRef(null);

    useEffect(() => {
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true }); // Alpha: true for transparent background
        renderer.setSize(window.innerWidth, window.innerHeight);
        mountRef.current.appendChild(renderer.domElement);


        // Half-sphere geometry
        const geometry = new THREE.SphereGeometry(5, 64, 32, 0, Math.PI);

        // Gradient material (more accurate to the image)
        const material = new THREE.ShaderMaterial({
            uniforms: {
                topColor: { value: new THREE.Color("#ffffff") }, // White
                bottomColor: { value: new THREE.Color("#ffe1f0") }, // Light pink  (adjust as needed)
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
                    float mixValue = vNormal.y * 0.5 + 0.5;  // 0.0 at bottom, 1.0 at top
                    vec3 color = mix(bottomColor, topColor, mixValue);
                    gl_FragColor = vec4(color, 1.0);  // Alpha is 1.0 (opaque)
                }
            `,
        });

        const globe = new THREE.Mesh(geometry, material);
        scene.add(globe);




        // Dotted effect (more control)
        const dotGeometry = new THREE.BufferGeometry();
        const numDots = 2000; // Increase for more dots
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
            color: 0x4d4d4d,   // Dark Gray
            size: 0.05,        // Adjust size
            transparent: true, // Enable transparency for smoother edges
        });
        const dots = new THREE.Points(dotGeometry, dotMaterial);
        scene.add(dots);



        // Orange dots (using spherical coordinates for placement on the globe)
        const createOrangeDot = (lat, lon) => { // Latitude, Longitude in radians
            const radius = 5.01; // Slightly above the surface
            const phi = (90 - lat) * Math.PI / 180;
            const theta = (lon + 180) * Math.PI / 180;


            const x = radius * Math.sin(phi) * Math.cos(theta);
            const y = radius * Math.cos(phi);
            const z = radius * Math.sin(phi) * Math.sin(theta);


            const dotGeometry = new THREE.SphereGeometry(0.1, 16, 8);
            const dotMaterial = new THREE.MeshBasicMaterial({ color: 0xff753d });  // Orange color
            const dot = new THREE.Mesh(dotGeometry, dotMaterial);
            dot.position.set(x, y, z);

            globe.add(dot);


        };


        createOrangeDot(40.7, -74);   // New York
        createOrangeDot(34, -118);  // Los Angeles (approx.)



        camera.position.z = 10;
        camera.position.y = 1;



        // OrbitControls (optional)
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.rotateSpeed = 0.5;


        const animate = () => {
            requestAnimationFrame(animate);
            controls.update();  // Update controls
            renderer.render(scene, camera);

        };

        animate();

        return () => {
            mountRef.current.removeChild(renderer.domElement);
        };


    }, []);


    return <div ref={mountRef} style={{ width: '100%', height: '500px' }} />;


};


export default Globe;