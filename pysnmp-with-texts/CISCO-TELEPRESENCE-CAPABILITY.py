#
# PySNMP MIB module CISCO-TELEPRESENCE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TELEPRESENCE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Bits, Gauge32, Integer32, ObjectIdentity, ModuleIdentity, MibIdentifier, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Bits", "Gauge32", "Integer32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTelepresenceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 565))
ciscoTelepresenceCapability.setRevisions(('2008-06-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTelepresenceCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTelepresenceCapability.setLastUpdated('200806050000Z')
if mibBuilder.loadTexts: ciscoTelepresenceCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTelepresenceCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: tb-sw@cisco.com')
if mibBuilder.loadTexts: ciscoTelepresenceCapability.setDescription('Agent capabilities for CISCO-TELEPRESENCE-MIB')
ciscoTelepresenceCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 565, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTSV120 = ciscoTelepresenceCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.4.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTSV120 = ciscoTelepresenceCapabilityCTSV120.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCapabilityCTSV120.setDescription('TELEPRESENCE MIB capabilities')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-CAPABILITY", ciscoTelepresenceCapabilityCTSV120=ciscoTelepresenceCapabilityCTSV120, ciscoTelepresenceCapability=ciscoTelepresenceCapability, PYSNMP_MODULE_ID=ciscoTelepresenceCapability)
