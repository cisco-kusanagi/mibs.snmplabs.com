#
# PySNMP MIB module CISCO-CAS-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CAS-IF-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:52:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Counter64, MibIdentifier, Bits, Counter32, NotificationType, Integer32, iso, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Counter64", "MibIdentifier", "Bits", "Counter32", "NotificationType", "Integer32", "iso", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCasIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 122))
ciscoCasIfCapability.setRevisions(('2009-12-04 00:00', '2004-08-10 00:00', '2003-12-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCasIfCapability.setRevisionsDescriptions(('Added capability statement ciscoCasIfCapabilityV12R04TPC3xxx.', 'Added ciscoCasIfCapabilityV5R015 for MGX8850 release 5.0.15.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCasIfCapability.setLastUpdated('200912040000Z')
if mibBuilder.loadTexts: ciscoCasIfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCasIfCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoCasIfCapability.setDescription('The agent capabilities for CISCO-CAS-IF-MIB.')
ciscoCasIfCapabilityV5R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R000 = ciscoCasIfCapabilityV5R000.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R000 = ciscoCasIfCapabilityV5R000.setStatus('current')
if mibBuilder.loadTexts: ciscoCasIfCapabilityV5R000.setDescription('CISCO-CAS-IF-MIB Capabilities for Voice Switch Service Module(VXSM) in Release 5.0.0.')
ciscoCasIfCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R015 = ciscoCasIfCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R015 = ciscoCasIfCapabilityV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoCasIfCapabilityV5R015.setDescription('CISCO-CAS-IF-MIB Capabilities for Voice Switch Service Module(VXSM) in Release 5.0.15.')
ciscoCasIfCapabilityV12R04TPC3xxx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV12R04TPC3xxx = ciscoCasIfCapabilityV12R04TPC3xxx.setProductRelease('CISCO IOS 12.4T for Integrate Service\n                     Router (ISR) c2xxx and c3xxx platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV12R04TPC3xxx = ciscoCasIfCapabilityV12R04TPC3xxx.setStatus('current')
if mibBuilder.loadTexts: ciscoCasIfCapabilityV12R04TPC3xxx.setDescription('CISCO-CAS-IF-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-CAS-IF-CAPABILITY", ciscoCasIfCapabilityV12R04TPC3xxx=ciscoCasIfCapabilityV12R04TPC3xxx, ciscoCasIfCapabilityV5R000=ciscoCasIfCapabilityV5R000, ciscoCasIfCapabilityV5R015=ciscoCasIfCapabilityV5R015, ciscoCasIfCapability=ciscoCasIfCapability, PYSNMP_MODULE_ID=ciscoCasIfCapability)
