#
# PySNMP MIB module CISCO-SYSAPPL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSAPPL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, IpAddress, MibIdentifier, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, iso, Counter64, Gauge32, ObjectIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "MibIdentifier", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "iso", "Counter64", "Gauge32", "ObjectIdentity", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSysApplCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoSysApplCapability.setRevisions(('2007-09-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSysApplCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSysApplCapability.setLastUpdated('200709140000Z')
if mibBuilder.loadTexts: ciscoSysApplCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSysApplCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSysApplCapability.setDescription('Agent capabilities for SYSAPPL-MIB')
ciscoSysApplCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysApplCapabilityCTSV120 = ciscoSysApplCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.2.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysApplCapabilityCTSV120 = ciscoSysApplCapabilityCTSV120.setStatus('current')
if mibBuilder.loadTexts: ciscoSysApplCapabilityCTSV120.setDescription('SYSAPPL MIB capabilities')
mibBuilder.exportSymbols("CISCO-SYSAPPL-CAPABILITY", ciscoSysApplCapabilityCTSV120=ciscoSysApplCapabilityCTSV120, PYSNMP_MODULE_ID=ciscoSysApplCapability, ciscoSysApplCapability=ciscoSysApplCapability)
