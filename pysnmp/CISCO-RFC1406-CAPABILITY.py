#
# PySNMP MIB module CISCO-RFC1406-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RFC1406-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, Bits, TimeTicks, iso, NotificationType, MibIdentifier, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Unsigned32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "TimeTicks", "iso", "NotificationType", "MibIdentifier", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Unsigned32", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRFC1406Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 102))
ciscoRFC1406Capability.setRevisions(('2002-10-22 00:00', '2001-08-17 00:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRFC1406Capability.setLastUpdated('200210220000Z')
if mibBuilder.loadTexts: ciscoRFC1406Capability.setOrganization('Cisco Systems, Inc.')
ciscoRFC1406CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV10R02 = ciscoRFC1406CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV10R02 = ciscoRFC1406CapabilityV10R02.setStatus('current')
ciscoRFC1406CapabilityV122R12T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12T = ciscoRFC1406CapabilityV122R12T.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12T = ciscoRFC1406CapabilityV122R12T.setStatus('obsolete')
ciscoRFC1406CapabilityV122R12TRev2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12TRev2 = ciscoRFC1406CapabilityV122R12TRev2.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12TRev2 = ciscoRFC1406CapabilityV122R12TRev2.setStatus('current')
mibBuilder.exportSymbols("CISCO-RFC1406-CAPABILITY", ciscoRFC1406CapabilityV122R12T=ciscoRFC1406CapabilityV122R12T, PYSNMP_MODULE_ID=ciscoRFC1406Capability, ciscoRFC1406CapabilityV10R02=ciscoRFC1406CapabilityV10R02, ciscoRFC1406CapabilityV122R12TRev2=ciscoRFC1406CapabilityV122R12TRev2, ciscoRFC1406Capability=ciscoRFC1406Capability)
