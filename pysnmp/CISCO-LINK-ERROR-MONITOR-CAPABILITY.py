#
# PySNMP MIB module CISCO-LINK-ERROR-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LINK-ERROR-MONITOR-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, iso, Gauge32, ObjectIdentity, Counter64, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Integer32, IpAddress, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Gauge32", "ObjectIdentity", "Counter64", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Integer32", "IpAddress", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLinkErrorMonitorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 414))
ciscoLinkErrorMonitorCapability.setRevisions(('2004-08-05 00:00',))
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setLastUpdated('200408050000Z')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setOrganization('Cisco Systems, Inc.')
clemCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 414, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemCapCatOSV08R0401 = clemCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemCapCatOSV08R0401 = clemCapCatOSV08R0401.setStatus('current')
mibBuilder.exportSymbols("CISCO-LINK-ERROR-MONITOR-CAPABILITY", clemCapCatOSV08R0401=clemCapCatOSV08R0401, ciscoLinkErrorMonitorCapability=ciscoLinkErrorMonitorCapability, PYSNMP_MODULE_ID=ciscoLinkErrorMonitorCapability)
