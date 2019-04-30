#
# PySNMP MIB module CISCO-TELEPRESENCE-CALL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TELEPRESENCE-CALL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Counter32, IpAddress, ModuleIdentity, NotificationType, MibIdentifier, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Counter32", "IpAddress", "ModuleIdentity", "NotificationType", "MibIdentifier", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTelepresenceCallCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 577))
ciscoTelepresenceCallCapability.setRevisions(('2011-02-02 00:00', '2008-11-30 00:00',))
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setLastUpdated('201102020000Z')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setOrganization('Cisco Systems, Inc.')
ciscoTelepresenceCallCapabilityCTSV150 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 577, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV150 = ciscoTelepresenceCallCapabilityCTSV150.setProductRelease('Cisco TelePresence System (CTS) 1.5.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV150 = ciscoTelepresenceCallCapabilityCTSV150.setStatus('current')
ciscoTelepresenceCallCapabilityCTSV170 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 577, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV170 = ciscoTelepresenceCallCapabilityCTSV170.setProductRelease('Cisco TelePresence System (CTS) 1.7.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV170 = ciscoTelepresenceCallCapabilityCTSV170.setStatus('current')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-CALL-CAPABILITY", PYSNMP_MODULE_ID=ciscoTelepresenceCallCapability, ciscoTelepresenceCallCapabilityCTSV170=ciscoTelepresenceCallCapabilityCTSV170, ciscoTelepresenceCallCapability=ciscoTelepresenceCallCapability, ciscoTelepresenceCallCapabilityCTSV150=ciscoTelepresenceCallCapabilityCTSV150)
