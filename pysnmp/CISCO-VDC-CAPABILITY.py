#
# PySNMP MIB module CISCO-VDC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VDC-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:01:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Counter32, Counter64, TimeTicks, ModuleIdentity, ObjectIdentity, Bits, iso, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Bits", "iso", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVdcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 621))
ciscoVdcCapability.setRevisions(('2013-07-26 00:00',))
if mibBuilder.loadTexts: ciscoVdcCapability.setLastUpdated('201307260000Z')
if mibBuilder.loadTexts: ciscoVdcCapability.setOrganization('Cisco Systems, Inc.')
ciscoVdcCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 621, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVdcCapNxOSV06R0202PN7k = ciscoVdcCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVdcCapNxOSV06R0202PN7k = ciscoVdcCapNxOSV06R0202PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-VDC-CAPABILITY", PYSNMP_MODULE_ID=ciscoVdcCapability, ciscoVdcCapability=ciscoVdcCapability, ciscoVdcCapNxOSV06R0202PN7k=ciscoVdcCapNxOSV06R0202PN7k)
