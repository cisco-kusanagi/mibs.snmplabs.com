#
# PySNMP MIB module CISCO-VISM-SESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-SESSION-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibIdentifier, iso, ModuleIdentity, NotificationType, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, ObjectIdentity, TimeTicks, Unsigned32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "ModuleIdentity", "NotificationType", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "ObjectIdentity", "TimeTicks", "Unsigned32", "Counter32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVismSessionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 415))
ciscoVismSessionCapability.setRevisions(('2005-09-19 00:00', '2004-09-03 00:00',))
if mibBuilder.loadTexts: ciscoVismSessionCapability.setLastUpdated('200509190000Z')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setOrganization('Cisco Systems, Inc.')
ciscoVismSessionCapV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 415, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV5R015 = ciscoVismSessionCapV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV5R015 = ciscoVismSessionCapV5R015.setStatus('current')
ciscoVismSessionCapV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 415, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV3325 = ciscoVismSessionCapV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV3325 = ciscoVismSessionCapV3325.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-SESSION-CAPABILITY", ciscoVismSessionCapV3325=ciscoVismSessionCapV3325, PYSNMP_MODULE_ID=ciscoVismSessionCapability, ciscoVismSessionCapV5R015=ciscoVismSessionCapV5R015, ciscoVismSessionCapability=ciscoVismSessionCapability)
