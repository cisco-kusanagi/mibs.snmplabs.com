#
# PySNMP MIB module CISCO-WDS-IDS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WDS-IDS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, NotificationType, Counter32, Unsigned32, Bits, Integer32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Counter64, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter32", "Unsigned32", "Bits", "Integer32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Counter64", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWdsidsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 424))
if mibBuilder.loadTexts: ciscoWdsidsCapability.setLastUpdated('200501130000Z')
if mibBuilder.loadTexts: ciscoWdsidsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWdsidsCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoWdsidsCapability.setDescription('Agent capabilities for CISCO-WDS-IDS-MIB')
ciscoWdsidsCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 424, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsidsCapabilityV1 = ciscoWdsidsCapabilityV1.setProductRelease('Cisco IOS 12.3(4) JA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsidsCapabilityV1 = ciscoWdsidsCapabilityV1.setStatus('current')
if mibBuilder.loadTexts: ciscoWdsidsCapabilityV1.setDescription('Cisco WDS IDS MIB capabilities')
mibBuilder.exportSymbols("CISCO-WDS-IDS-CAPABILITY", ciscoWdsidsCapability=ciscoWdsidsCapability, ciscoWdsidsCapabilityV1=ciscoWdsidsCapabilityV1, PYSNMP_MODULE_ID=ciscoWdsidsCapability)
