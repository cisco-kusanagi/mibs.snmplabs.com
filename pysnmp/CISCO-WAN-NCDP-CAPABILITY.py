#
# PySNMP MIB module CISCO-WAN-NCDP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-NCDP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Integer32, Unsigned32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Bits, Gauge32, IpAddress, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Integer32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Bits", "Gauge32", "IpAddress", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanNcdpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
if mibBuilder.loadTexts: ciscoWanNcdpCapability.setLastUpdated('200109140000Z')
if mibBuilder.loadTexts: ciscoWanNcdpCapability.setOrganization('Cisco Systems, Inc.')
ciscoWanNcdpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanNcdpCapabilityV3R00 = ciscoWanNcdpCapabilityV3R00.setProductRelease('MGX8850 Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanNcdpCapabilityV3R00 = ciscoWanNcdpCapabilityV3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-NCDP-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanNcdpCapability, ciscoWanNcdpCapabilityV3R00=ciscoWanNcdpCapabilityV3R00, ciscoWanNcdpCapability=ciscoWanNcdpCapability)
