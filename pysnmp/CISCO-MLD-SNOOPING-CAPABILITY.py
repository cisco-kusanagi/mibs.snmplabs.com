#
# PySNMP MIB module CISCO-MLD-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MLD-SNOOPING-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter64, TimeTicks, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Integer32, Unsigned32, Bits, IpAddress, Counter32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Integer32", "Unsigned32", "Bits", "IpAddress", "Counter32", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMldSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 586))
ciscoMldSnoopingCapability.setRevisions(('2010-03-02 00:00',))
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setLastUpdated('201003020000Z')
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setOrganization('Cisco Systems, Inc.')
ciscoMldSnoopingCapabilityV04R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 586, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMldSnoopingCapabilityV04R01 = ciscoMldSnoopingCapabilityV04R01.setProductRelease('Cisco IOS-XR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMldSnoopingCapabilityV04R01 = ciscoMldSnoopingCapabilityV04R01.setStatus('current')
mibBuilder.exportSymbols("CISCO-MLD-SNOOPING-CAPABILITY", ciscoMldSnoopingCapabilityV04R01=ciscoMldSnoopingCapabilityV04R01, PYSNMP_MODULE_ID=ciscoMldSnoopingCapability, ciscoMldSnoopingCapability=ciscoMldSnoopingCapability)
