#
# PySNMP MIB module CISCO-SYSAPPL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSAPPL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, MibIdentifier, ModuleIdentity, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, IpAddress, iso, Unsigned32, Integer32, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "IpAddress", "iso", "Unsigned32", "Integer32", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSysApplCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoSysApplCapability.setRevisions(('2007-09-14 00:00',))
if mibBuilder.loadTexts: ciscoSysApplCapability.setLastUpdated('200709140000Z')
if mibBuilder.loadTexts: ciscoSysApplCapability.setOrganization('Cisco Systems, Inc.')
ciscoSysApplCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysApplCapabilityCTSV120 = ciscoSysApplCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.2.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysApplCapabilityCTSV120 = ciscoSysApplCapabilityCTSV120.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSAPPL-CAPABILITY", ciscoSysApplCapabilityCTSV120=ciscoSysApplCapabilityCTSV120, ciscoSysApplCapability=ciscoSysApplCapability, PYSNMP_MODULE_ID=ciscoSysApplCapability)
