#
# PySNMP MIB module CISCO-MGC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGC-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, ObjectIdentity, Unsigned32, TimeTicks, Integer32, NotificationType, MibIdentifier, Counter32, Gauge32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "Unsigned32", "TimeTicks", "Integer32", "NotificationType", "MibIdentifier", "Counter32", "Gauge32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 370))
ciscoMgcCapability.setRevisions(('2004-02-05 00:00',))
if mibBuilder.loadTexts: ciscoMgcCapability.setLastUpdated('200402050000Z')
if mibBuilder.loadTexts: ciscoMgcCapability.setOrganization('Cisco Systems, Inc.')
ciscoMgcCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 370, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgcCapabilityV5R00 = ciscoMgcCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgcCapabilityV5R00 = ciscoMgcCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGC-CAPABILITY", PYSNMP_MODULE_ID=ciscoMgcCapability, ciscoMgcCapabilityV5R00=ciscoMgcCapabilityV5R00, ciscoMgcCapability=ciscoMgcCapability)
