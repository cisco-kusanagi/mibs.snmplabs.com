#
# PySNMP MIB module CISCO-VISM-SESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-SESSION-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:18:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Unsigned32, Bits, ModuleIdentity, Integer32, NotificationType, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Unsigned32", "Bits", "ModuleIdentity", "Integer32", "NotificationType", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismSessionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 415))
ciscoVismSessionCapability.setRevisions(('2005-09-19 00:00', '2004-09-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismSessionCapability.setRevisionsDescriptions(('Added capabilities for VISM Release 3.3.25.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVismSessionCapability.setLastUpdated('200509190000Z')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setDescription('This MIB defines the agent capabilities for CISCO-VISM-SESSION-MIB.')
ciscoVismSessionCapV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 415, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV5R015 = ciscoVismSessionCapV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV5R015 = ciscoVismSessionCapV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoVismSessionCapV5R015.setDescription('Agent capabilities for Voice Switch Service Module (VXSM) in MGX8850 release 5.0.15.')
ciscoVismSessionCapV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 415, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV3325 = ciscoVismSessionCapV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV3325 = ciscoVismSessionCapV3325.setStatus('current')
if mibBuilder.loadTexts: ciscoVismSessionCapV3325.setDescription('CISCO-VISM-SESSION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VISM-SESSION-CAPABILITY", PYSNMP_MODULE_ID=ciscoVismSessionCapability, ciscoVismSessionCapability=ciscoVismSessionCapability, ciscoVismSessionCapV3325=ciscoVismSessionCapV3325, ciscoVismSessionCapV5R015=ciscoVismSessionCapV5R015)
