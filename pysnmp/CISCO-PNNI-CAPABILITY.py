#
# PySNMP MIB module CISCO-PNNI-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PNNI-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter64, ModuleIdentity, TimeTicks, IpAddress, NotificationType, iso, Integer32, Bits, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "TimeTicks", "IpAddress", "NotificationType", "iso", "Integer32", "Bits", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPnniCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoPnniCapability.setRevisions(('2002-05-02 00:00',))
if mibBuilder.loadTexts: ciscoPnniCapability.setLastUpdated('200205020000Z')
if mibBuilder.loadTexts: ciscoPnniCapability.setOrganization('Cisco Systems, Inc.')
ciscoPnniCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPnniCapabilityV2R00 = ciscoPnniCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPnniCapabilityV2R00 = ciscoPnniCapabilityV2R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-PNNI-CAPABILITY", PYSNMP_MODULE_ID=ciscoPnniCapability, ciscoPnniCapability=ciscoPnniCapability, ciscoPnniCapabilityV2R00=ciscoPnniCapabilityV2R00)
