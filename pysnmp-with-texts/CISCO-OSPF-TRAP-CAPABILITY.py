#
# PySNMP MIB module CISCO-OSPF-TRAP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OSPF-TRAP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:08:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, IpAddress, TimeTicks, Gauge32, Counter32, ModuleIdentity, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "TimeTicks", "Gauge32", "Counter32", "ModuleIdentity", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoOspfTrapCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 288))
ciscoOspfTrapCapability.setRevisions(('2002-11-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoOspfTrapCapability.setRevisionsDescriptions(('Initial version of the MIB Module',))
if mibBuilder.loadTexts: ciscoOspfTrapCapability.setLastUpdated('200211240000Z')
if mibBuilder.loadTexts: ciscoOspfTrapCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoOspfTrapCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134, USA Tel: +1 800 553-NETS E-mail: cs-ospf@cisco.com')
if mibBuilder.loadTexts: ciscoOspfTrapCapability.setDescription('Agent capabilities for the OSPF TRAP MIB.')
ciscoOspfTrapCapabilityV12R026S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 288, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOspfTrapCapabilityV12R026S = ciscoOspfTrapCapabilityV12R026S.setProductRelease('Cisco IOS 12.0(26)S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOspfTrapCapabilityV12R026S = ciscoOspfTrapCapabilityV12R026S.setStatus('current')
if mibBuilder.loadTexts: ciscoOspfTrapCapabilityV12R026S.setDescription('CISCO-OSPF-TRAP-MIB capabilites')
mibBuilder.exportSymbols("CISCO-OSPF-TRAP-CAPABILITY", ciscoOspfTrapCapabilityV12R026S=ciscoOspfTrapCapabilityV12R026S, PYSNMP_MODULE_ID=ciscoOspfTrapCapability, ciscoOspfTrapCapability=ciscoOspfTrapCapability)
