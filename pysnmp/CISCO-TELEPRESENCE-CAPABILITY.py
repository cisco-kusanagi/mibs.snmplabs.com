#
# PySNMP MIB module CISCO-TELEPRESENCE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TELEPRESENCE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ObjectIdentity, Unsigned32, TimeTicks, MibIdentifier, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, iso, NotificationType, Bits, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "TimeTicks", "MibIdentifier", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "iso", "NotificationType", "Bits", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTelepresenceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 565))
ciscoTelepresenceCapability.setRevisions(('2008-06-05 00:00',))
if mibBuilder.loadTexts: ciscoTelepresenceCapability.setLastUpdated('200806050000Z')
if mibBuilder.loadTexts: ciscoTelepresenceCapability.setOrganization('Cisco Systems, Inc.')
ciscoTelepresenceCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 565, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTSV120 = ciscoTelepresenceCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.4.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTSV120 = ciscoTelepresenceCapabilityCTSV120.setStatus('current')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-CAPABILITY", PYSNMP_MODULE_ID=ciscoTelepresenceCapability, ciscoTelepresenceCapability=ciscoTelepresenceCapability, ciscoTelepresenceCapabilityCTSV120=ciscoTelepresenceCapabilityCTSV120)
