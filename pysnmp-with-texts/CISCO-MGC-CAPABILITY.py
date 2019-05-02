#
# PySNMP MIB module CISCO-MGC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGC-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, Gauge32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Integer32, TimeTicks, Counter32, ObjectIdentity, Bits, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Integer32", "TimeTicks", "Counter32", "ObjectIdentity", "Bits", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMgcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 370))
ciscoMgcCapability.setRevisions(('2004-02-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMgcCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMgcCapability.setLastUpdated('200402050000Z')
if mibBuilder.loadTexts: ciscoMgcCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMgcCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoMgcCapability.setDescription('The agent capabilities for CISCO-MGC-MIB.')
ciscoMgcCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 370, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgcCapabilityV5R00 = ciscoMgcCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgcCapabilityV5R00 = ciscoMgcCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoMgcCapabilityV5R00.setDescription('Agent capabilities for VXSM in release 5.0.0.')
mibBuilder.exportSymbols("CISCO-MGC-CAPABILITY", ciscoMgcCapabilityV5R00=ciscoMgcCapabilityV5R00, ciscoMgcCapability=ciscoMgcCapability, PYSNMP_MODULE_ID=ciscoMgcCapability)
