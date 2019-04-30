#
# PySNMP MIB module CISCO-COMMON-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-COMMON-MGMT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, NotificationType, Counter32, MibIdentifier, iso, Unsigned32, ModuleIdentity, TimeTicks, ObjectIdentity, IpAddress, Counter64, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter32", "MibIdentifier", "iso", "Unsigned32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "IpAddress", "Counter64", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCommonMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 448))
ciscoCommonMgmtCapability.setRevisions(('2005-08-27 00:00',))
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setLastUpdated('200508270000Z')
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setOrganization('Cisco Systems, Inc.')
ciscoCommonMgmtCapMDS30R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 448, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonMgmtCapMDS30R1 = ciscoCommonMgmtCapMDS30R1.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonMgmtCapMDS30R1 = ciscoCommonMgmtCapMDS30R1.setStatus('current')
mibBuilder.exportSymbols("CISCO-COMMON-MGMT-CAPABILITY", PYSNMP_MODULE_ID=ciscoCommonMgmtCapability, ciscoCommonMgmtCapMDS30R1=ciscoCommonMgmtCapMDS30R1, ciscoCommonMgmtCapability=ciscoCommonMgmtCapability)
