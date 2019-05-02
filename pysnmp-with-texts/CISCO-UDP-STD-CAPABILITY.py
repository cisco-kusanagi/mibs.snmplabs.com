#
# PySNMP MIB module CISCO-UDP-STD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UDP-STD-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, Counter64, iso, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, ModuleIdentity, Unsigned32, TimeTicks, Bits, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "iso", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "ModuleIdentity", "Unsigned32", "TimeTicks", "Bits", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoUdpStdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 482))
ciscoUdpStdCapability.setRevisions(('2008-06-30 00:00', '2006-11-08 00:00', '2006-05-26 00:00', '2006-02-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoUdpStdCapability.setRevisionsDescriptions(('Added ciscoUdpStdCapc4710aceVA1R700 agent capability for ACE 4710 Application Control Engine Appliance.', 'Added agent capability for IOS XR 3.4', 'Added capability statement ciscoUdpStdCapACSWV03R000.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoUdpStdCapability.setLastUpdated('200806300000Z')
if mibBuilder.loadTexts: ciscoUdpStdCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoUdpStdCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoUdpStdCapability.setDescription('Agent capabilities for UDP-MIB')
ciscoUdpStdCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R2CRS1 = ciscoUdpStdCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R2CRS1 = ciscoUdpStdCapIOSXRV3R2CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoUdpStdCapIOSXRV3R2CRS1.setDescription('UDP-MIB capabilities for IOS XR release 3.2.0')
ciscoUdpStdCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapACSWV03R000 = ciscoUdpStdCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                     for Application Control Engine(ACE) \n                     Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapACSWV03R000 = ciscoUdpStdCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoUdpStdCapACSWV03R000.setDescription('UDP-MIB capabilities for ACSW 3.0')
ciscoUdpStdCapIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R4CRS1 = ciscoUdpStdCapIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapIOSXRV3R4CRS1 = ciscoUdpStdCapIOSXRV3R4CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoUdpStdCapIOSXRV3R4CRS1.setDescription('UDP-MIB capabilities for IOS XR release 3.4')
ciscoUdpStdCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 482, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapc4710aceVA1R700 = ciscoUdpStdCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdpStdCapc4710aceVA1R700 = ciscoUdpStdCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoUdpStdCapc4710aceVA1R700.setDescription('UDP-MIB capabilities for ACSW A1(7).')
mibBuilder.exportSymbols("CISCO-UDP-STD-CAPABILITY", ciscoUdpStdCapability=ciscoUdpStdCapability, ciscoUdpStdCapc4710aceVA1R700=ciscoUdpStdCapc4710aceVA1R700, ciscoUdpStdCapIOSXRV3R4CRS1=ciscoUdpStdCapIOSXRV3R4CRS1, ciscoUdpStdCapIOSXRV3R2CRS1=ciscoUdpStdCapIOSXRV3R2CRS1, ciscoUdpStdCapACSWV03R000=ciscoUdpStdCapACSWV03R000, PYSNMP_MODULE_ID=ciscoUdpStdCapability)
