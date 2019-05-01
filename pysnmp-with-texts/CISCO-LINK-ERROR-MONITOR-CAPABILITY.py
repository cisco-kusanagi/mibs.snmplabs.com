#
# PySNMP MIB module CISCO-LINK-ERROR-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LINK-ERROR-MONITOR-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:04:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, Bits, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, IpAddress, MibIdentifier, iso, NotificationType, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Bits", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "iso", "NotificationType", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLinkErrorMonitorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 414))
ciscoLinkErrorMonitorCapability.setRevisions(('2004-08-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setLastUpdated('200408050000Z')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setDescription('This MIB module describes the capability of CISCO-LINK-ERROR-MONITOR-MIB.')
clemCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 414, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemCapCatOSV08R0401 = clemCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemCapCatOSV08R0401 = clemCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: clemCapCatOSV08R0401.setDescription('CISCO-LINK-ERROR-MONITOR-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-LINK-ERROR-MONITOR-CAPABILITY", ciscoLinkErrorMonitorCapability=ciscoLinkErrorMonitorCapability, PYSNMP_MODULE_ID=ciscoLinkErrorMonitorCapability, clemCapCatOSV08R0401=clemCapCatOSV08R0401)
