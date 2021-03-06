#
# PySNMP MIB module RIVERSTONE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
riverstoneProducts, = mibBuilder.importSymbols("RSTONE-SMI-MIB", "riverstoneProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Integer32, iso, Counter32, Counter64, ModuleIdentity, NotificationType, Bits, MibIdentifier, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Integer32", "iso", "Counter32", "Counter64", "ModuleIdentity", "NotificationType", "Bits", "MibIdentifier", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsFamilyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1))
rsFamilyMIB.setRevisions(('2000-04-16 00:00', '2000-11-28 00:00', '2000-11-29 00:00', '2000-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsFamilyMIB.setRevisionsDescriptions(('Riverstone RS Family of products object IDs added.', 'Riverstone RS1000 object ID added. Changed IA1000->IA1100, IA1100->IA1200(typo)', 'Riverstone IA1500 object ID added.', 'Riverstone RS38000 object ID added.',))
if mibBuilder.loadTexts: rsFamilyMIB.setLastUpdated('200011300000Z')
if mibBuilder.loadTexts: rsFamilyMIB.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: rsFamilyMIB.setContactInfo('Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA USA 95054 PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: rsFamilyMIB.setDescription('This mib module defines system Object Identifier values for sysObjectID.0 for network elements manufactured and sold by Riverstone Networks, Inc http://www.riverstonenet.com/products. Contains sysObjectIDs for RS Procut Line of Multi Layer Switch Routers. Copyright (C) Riverstone Networks, Inc 2000')
rs8000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 1))
if mibBuilder.loadTexts: rs8000.setStatus('current')
if mibBuilder.loadTexts: rs8000.setDescription('RS 8000 8-slot switch router. http://www.riverstonenet.com/products/RS8x00/rs8x00.html')
rs8600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 2))
if mibBuilder.loadTexts: rs8600.setStatus('current')
if mibBuilder.loadTexts: rs8600.setDescription('RS 8000 16-slot switch router. http://www.riverstonenet.com/products/RS8x00/rs8x00.html')
rs2000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 3))
if mibBuilder.loadTexts: rs2000.setStatus('current')
if mibBuilder.loadTexts: rs2000.setDescription('RS 2000 2-slot switch router with fixed 16 port 10/100 Ethernet TX http://www.riverstonenet.com/products/RS2x00')
rs2100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 4))
if mibBuilder.loadTexts: rs2100.setStatus('current')
if mibBuilder.loadTexts: rs2100.setDescription('RS 2100 Fixed 8 Port Gigabit Ethernet SX http://www.riverstonenet.com/products/RS2x00')
rs3000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 5))
if mibBuilder.loadTexts: rs3000.setStatus('current')
if mibBuilder.loadTexts: rs3000.setDescription('RS 3000 2-slot switch router with fixed 16 port 10/100 Ethernet TX. http://www.riverstonenet.com/products/RS3000')
rs32000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 6))
if mibBuilder.loadTexts: rs32000.setStatus('current')
if mibBuilder.loadTexts: rs32000.setDescription('RS 32000 16-slot 500 10/100 or 120 GigEthernet switch router. http://www.riverstonenet.com/products/RS32000')
rs1000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 8))
if mibBuilder.loadTexts: rs1000.setStatus('current')
if mibBuilder.loadTexts: rs1000.setDescription('RS 1000 2-slot switch router http://www.riverstonenet.com/products/RS1000')
rs38000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 9))
if mibBuilder.loadTexts: rs38000.setStatus('current')
if mibBuilder.loadTexts: rs38000.setDescription('RS 38000 16-slot 500 10/100 or 120 GigEthernet wire-speed switch router. http://www.riverstonenet.com/products/RS38000')
rsIA1100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 22))
if mibBuilder.loadTexts: rsIA1100.setStatus('current')
if mibBuilder.loadTexts: rsIA1100.setDescription('IA 1100 2-slot load balancer with fixed 16 port 10/100 Ethernet TX http://www.riverstonenet.com/products/internet-appliance')
rsIA1200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 23))
if mibBuilder.loadTexts: rsIA1200.setStatus('current')
if mibBuilder.loadTexts: rsIA1200.setDescription('IA 1200 Fixed 8 port Gigabit Ethernet load balancer http://www.riverstonenet.com/products/internet-appliance')
rsIA1500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1, 1, 27))
if mibBuilder.loadTexts: rsIA1500.setStatus('current')
if mibBuilder.loadTexts: rsIA1500.setDescription('IA 1500 2-slot load balancer http://www.riverstonenet.com/products/internet-appliance')
mibBuilder.exportSymbols("RIVERSTONE-PRODUCTS-MIB", rs32000=rs32000, PYSNMP_MODULE_ID=rsFamilyMIB, rsFamilyMIB=rsFamilyMIB, rs8000=rs8000, rs3000=rs3000, rs38000=rs38000, rsIA1500=rsIA1500, rs8600=rs8600, rs2100=rs2100, rs1000=rs1000, rsIA1100=rsIA1100, rs2000=rs2000, rsIA1200=rsIA1200)
