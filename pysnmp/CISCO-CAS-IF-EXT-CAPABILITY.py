#
# PySNMP MIB module CISCO-CAS-IF-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CAS-IF-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:35:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, MibIdentifier, IpAddress, Bits, TimeTicks, Counter64, Gauge32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "IpAddress", "Bits", "TimeTicks", "Counter64", "Gauge32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCasIfExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 349))
ciscoCasIfExtCapability.setRevisions(('2004-01-19 00:00',))
if mibBuilder.loadTexts: ciscoCasIfExtCapability.setLastUpdated('200401190000Z')
if mibBuilder.loadTexts: ciscoCasIfExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoCasIfExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 349, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfExtCapabilityV5R00 = ciscoCasIfExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfExtCapabilityV5R00 = ciscoCasIfExtCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-CAS-IF-EXT-CAPABILITY", ciscoCasIfExtCapabilityV5R00=ciscoCasIfExtCapabilityV5R00, ciscoCasIfExtCapability=ciscoCasIfExtCapability, PYSNMP_MODULE_ID=ciscoCasIfExtCapability)
