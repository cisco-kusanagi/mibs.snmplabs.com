#
# PySNMP MIB module CISCO-SNMP-TARGET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-TARGET-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, Counter32, IpAddress, TimeTicks, Integer32, Unsigned32, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Counter32", "IpAddress", "TimeTicks", "Integer32", "Unsigned32", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSnmpTargetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 359))
ciscoSnmpTargetCapability.setRevisions(('2008-07-21 00:00', '2007-06-22 00:00', '2006-04-11 00:00', '2004-07-28 00:00', '2003-09-16 00:00',))
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setLastUpdated('200807210000Z')
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setOrganization('Cisco Systems, Inc.')
ciscoSnmpTargetCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapCatOSV05R0501 = ciscoSnmpTargetCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapCatOSV05R0501 = ciscoSnmpTargetCapCatOSV05R0501.setStatus('current')
ciscoSnmpTargetCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapVISM33 = ciscoSnmpTargetCapVISM33.setProductRelease('Cisco VISM Release 3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapVISM33 = ciscoSnmpTargetCapVISM33.setStatus('current')
ciscoSnmpTargetCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapACSWV03R000 = ciscoSnmpTargetCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapACSWV03R000 = ciscoSnmpTargetCapACSWV03R000.setStatus('current')
ciscoSnmpTargetCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapc4710aceVA1R700 = ciscoSnmpTargetCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapc4710aceVA1R700 = ciscoSnmpTargetCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-TARGET-CAPABILITY", ciscoSnmpTargetCapability=ciscoSnmpTargetCapability, ciscoSnmpTargetCapc4710aceVA1R700=ciscoSnmpTargetCapc4710aceVA1R700, ciscoSnmpTargetCapCatOSV05R0501=ciscoSnmpTargetCapCatOSV05R0501, ciscoSnmpTargetCapACSWV03R000=ciscoSnmpTargetCapACSWV03R000, ciscoSnmpTargetCapVISM33=ciscoSnmpTargetCapVISM33, PYSNMP_MODULE_ID=ciscoSnmpTargetCapability)
