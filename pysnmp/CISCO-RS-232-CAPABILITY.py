#
# PySNMP MIB module CISCO-RS-232-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RS-232-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, iso, TimeTicks, Gauge32, Integer32, IpAddress, Counter64, NotificationType, MibIdentifier, Unsigned32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "iso", "TimeTicks", "Gauge32", "Integer32", "IpAddress", "Counter64", "NotificationType", "MibIdentifier", "Unsigned32", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRS232Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 115))
ciscoRS232Capability.setRevisions(('2002-05-16 00:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRS232Capability.setLastUpdated('200205160000Z')
if mibBuilder.loadTexts: ciscoRS232Capability.setOrganization('Cisco Systems, Inc.')
ciscoRS232CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 115, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV10R02 = ciscoRS232CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV10R02 = ciscoRS232CapabilityV10R02.setStatus('current')
ciscoRS232CapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 115, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV2R00 = ciscoRS232CapabilityV2R00.setProductRelease('MGX8850 Release 2.0,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV2R00 = ciscoRS232CapabilityV2R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-RS-232-CAPABILITY", ciscoRS232CapabilityV10R02=ciscoRS232CapabilityV10R02, PYSNMP_MODULE_ID=ciscoRS232Capability, ciscoRS232Capability=ciscoRS232Capability, ciscoRS232CapabilityV2R00=ciscoRS232CapabilityV2R00)
