#
# PySNMP MIB module CISCO-CAS-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CAS-IF-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:35:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, iso, ObjectIdentity, Unsigned32, IpAddress, Bits, MibIdentifier, Counter64, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "iso", "ObjectIdentity", "Unsigned32", "IpAddress", "Bits", "MibIdentifier", "Counter64", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCasIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 122))
ciscoCasIfCapability.setRevisions(('2009-12-04 00:00', '2004-08-10 00:00', '2003-12-03 00:00',))
if mibBuilder.loadTexts: ciscoCasIfCapability.setLastUpdated('200912040000Z')
if mibBuilder.loadTexts: ciscoCasIfCapability.setOrganization('Cisco Systems, Inc.')
ciscoCasIfCapabilityV5R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R000 = ciscoCasIfCapabilityV5R000.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R000 = ciscoCasIfCapabilityV5R000.setStatus('current')
ciscoCasIfCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R015 = ciscoCasIfCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R015 = ciscoCasIfCapabilityV5R015.setStatus('current')
ciscoCasIfCapabilityV12R04TPC3xxx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV12R04TPC3xxx = ciscoCasIfCapabilityV12R04TPC3xxx.setProductRelease('CISCO IOS 12.4T for Integrate Service\n                     Router (ISR) c2xxx and c3xxx platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV12R04TPC3xxx = ciscoCasIfCapabilityV12R04TPC3xxx.setStatus('current')
mibBuilder.exportSymbols("CISCO-CAS-IF-CAPABILITY", ciscoCasIfCapabilityV5R015=ciscoCasIfCapabilityV5R015, ciscoCasIfCapability=ciscoCasIfCapability, ciscoCasIfCapabilityV5R000=ciscoCasIfCapabilityV5R000, PYSNMP_MODULE_ID=ciscoCasIfCapability, ciscoCasIfCapabilityV12R04TPC3xxx=ciscoCasIfCapabilityV12R04TPC3xxx)
