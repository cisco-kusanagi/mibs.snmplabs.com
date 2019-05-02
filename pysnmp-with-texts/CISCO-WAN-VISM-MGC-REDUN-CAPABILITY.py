#
# PySNMP MIB module CISCO-WAN-VISM-MGC-REDUN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-MGC-REDUN-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, Counter32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, Integer32, TimeTicks, Bits, Gauge32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "Integer32", "TimeTicks", "Bits", "Gauge32", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanVismMgcRedunCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 338))
ciscoWanVismMgcRedunCapability.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setLastUpdated('200108220000Z')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setDescription('The Agent Capabilities for CISCO-WAN-MGC-REDUN-MIB ')
ciscoWanVismMgcRedunCapV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 338, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgcRedunCapV2R00 = ciscoWanVismMgcRedunCapV2R00.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgcRedunCapV2R00 = ciscoWanVismMgcRedunCapV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapV2R00.setDescription('CISCO-WAN-VISM-MGC-REDUN-MIB capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-MGC-REDUN-CAPABILITY", ciscoWanVismMgcRedunCapV2R00=ciscoWanVismMgcRedunCapV2R00, PYSNMP_MODULE_ID=ciscoWanVismMgcRedunCapability, ciscoWanVismMgcRedunCapability=ciscoWanVismMgcRedunCapability)
