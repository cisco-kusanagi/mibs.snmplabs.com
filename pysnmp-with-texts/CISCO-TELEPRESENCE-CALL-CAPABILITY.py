#
# PySNMP MIB module CISCO-TELEPRESENCE-CALL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TELEPRESENCE-CALL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter64, ModuleIdentity, Bits, Unsigned32, TimeTicks, Integer32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, ObjectIdentity, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Bits", "Unsigned32", "TimeTicks", "Integer32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "ObjectIdentity", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoTelepresenceCallCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 577))
ciscoTelepresenceCallCapability.setRevisions(('2011-02-02 00:00', '2008-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setRevisionsDescriptions(('Added capability for Cisco Telepresence System (CTS) 1.7.0.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setLastUpdated('201102020000Z')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: tsbu-snmp-dev@cisco.com')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setDescription('Agent capabilities for CISCO-TELEPRESENCE-CALL-MIB')
ciscoTelepresenceCallCapabilityCTSV150 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 577, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV150 = ciscoTelepresenceCallCapabilityCTSV150.setProductRelease('Cisco TelePresence System (CTS) 1.5.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV150 = ciscoTelepresenceCallCapabilityCTSV150.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapabilityCTSV150.setDescription('TELEPRESENCE CALL MIB capabilities')
ciscoTelepresenceCallCapabilityCTSV170 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 577, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV170 = ciscoTelepresenceCallCapabilityCTSV170.setProductRelease('Cisco TelePresence System (CTS) 1.7.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV170 = ciscoTelepresenceCallCapabilityCTSV170.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapabilityCTSV170.setDescription('TELEPRESENCE CALL MIB capabilities')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-CALL-CAPABILITY", ciscoTelepresenceCallCapability=ciscoTelepresenceCallCapability, ciscoTelepresenceCallCapabilityCTSV170=ciscoTelepresenceCallCapabilityCTSV170, ciscoTelepresenceCallCapabilityCTSV150=ciscoTelepresenceCallCapabilityCTSV150, PYSNMP_MODULE_ID=ciscoTelepresenceCallCapability)
