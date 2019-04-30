#
# PySNMP MIB module CISCO-MODEM-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MODEM-MGMT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, TimeTicks, Integer32, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, ModuleIdentity, NotificationType, Gauge32, Counter64, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Integer32", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "ModuleIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoModemMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoModemMgmtCapability.setRevisions(('2006-07-31 00:00',))
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setLastUpdated('200607310000Z')
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setOrganization('Cisco Systems, Inc.')
ciscoModemMgmtCapV12R4TISR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModemMgmtCapV12R4TISR = ciscoModemMgmtCapV12R4TISR.setProductRelease('Cisco IOS 12.4 for ATG Platform Devices')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModemMgmtCapV12R4TISR = ciscoModemMgmtCapV12R4TISR.setStatus('current')
mibBuilder.exportSymbols("CISCO-MODEM-MGMT-CAPABILITY", ciscoModemMgmtCapability=ciscoModemMgmtCapability, ciscoModemMgmtCapV12R4TISR=ciscoModemMgmtCapV12R4TISR, PYSNMP_MODULE_ID=ciscoModemMgmtCapability)
