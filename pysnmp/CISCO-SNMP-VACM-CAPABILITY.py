#
# PySNMP MIB module CISCO-SNMP-VACM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-VACM-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, ModuleIdentity, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, iso, NotificationType, Unsigned32, MibIdentifier, Bits, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "iso", "NotificationType", "Unsigned32", "MibIdentifier", "Bits", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpVacmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 333))
ciscoSnmpVacmCapability.setRevisions(('2008-08-04 00:00', '2007-06-22 00:00', '2006-05-22 00:00', '2003-09-05 00:00',))
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setOrganization('Cisco Systems, Inc.')
ciscoSnmpVacmCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapCatOSV05R0501 = ciscoSnmpVacmCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapCatOSV05R0501 = ciscoSnmpVacmCapCatOSV05R0501.setStatus('current')
ciscoSnmpVacmCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapACSWV03R000 = ciscoSnmpVacmCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapACSWV03R000 = ciscoSnmpVacmCapACSWV03R000.setStatus('current')
ciscoSnmpVacmCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapc4710aceVA1R700 = ciscoSnmpVacmCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapc4710aceVA1R700 = ciscoSnmpVacmCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-VACM-CAPABILITY", ciscoSnmpVacmCapACSWV03R000=ciscoSnmpVacmCapACSWV03R000, ciscoSnmpVacmCapability=ciscoSnmpVacmCapability, ciscoSnmpVacmCapCatOSV05R0501=ciscoSnmpVacmCapCatOSV05R0501, PYSNMP_MODULE_ID=ciscoSnmpVacmCapability, ciscoSnmpVacmCapc4710aceVA1R700=ciscoSnmpVacmCapc4710aceVA1R700)
