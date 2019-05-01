#
# PySNMP MIB module CISCO-RFC1406-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RFC1406-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, iso, Unsigned32, IpAddress, ObjectIdentity, ModuleIdentity, NotificationType, Counter32, MibIdentifier, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Unsigned32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Counter32", "MibIdentifier", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRFC1406Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 102))
ciscoRFC1406Capability.setRevisions(('2002-10-22 00:00', '2001-08-17 00:00', '1994-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRFC1406Capability.setRevisionsDescriptions(('Support SET operation for dsx1LineCoding and dsx1LineType', 'Support SET operation for dsx1LoopbackConfig object.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRFC1406Capability.setLastUpdated('200210220000Z')
if mibBuilder.loadTexts: ciscoRFC1406Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRFC1406Capability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRFC1406Capability.setDescription('Agent capabilities for RFC1406-MIB (DS1 MIB)')
ciscoRFC1406CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV10R02 = ciscoRFC1406CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV10R02 = ciscoRFC1406CapabilityV10R02.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1406CapabilityV10R02.setDescription('ds1 capabilities')
ciscoRFC1406CapabilityV122R12T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12T = ciscoRFC1406CapabilityV122R12T.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12T = ciscoRFC1406CapabilityV122R12T.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoRFC1406CapabilityV122R12T.setDescription('ds1 capabilities')
ciscoRFC1406CapabilityV122R12TRev2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12TRev2 = ciscoRFC1406CapabilityV122R12TRev2.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12TRev2 = ciscoRFC1406CapabilityV122R12TRev2.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1406CapabilityV122R12TRev2.setDescription('ds1 capabilities')
mibBuilder.exportSymbols("CISCO-RFC1406-CAPABILITY", PYSNMP_MODULE_ID=ciscoRFC1406Capability, ciscoRFC1406CapabilityV122R12TRev2=ciscoRFC1406CapabilityV122R12TRev2, ciscoRFC1406CapabilityV10R02=ciscoRFC1406CapabilityV10R02, ciscoRFC1406Capability=ciscoRFC1406Capability, ciscoRFC1406CapabilityV122R12T=ciscoRFC1406CapabilityV122R12T)
