#
# PySNMP MIB module CISCO-SNMP-NOTIFICATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-NOTIFICATION-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, Gauge32, ModuleIdentity, IpAddress, MibIdentifier, Counter64, Bits, TimeTicks, NotificationType, iso, ObjectIdentity, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "ModuleIdentity", "IpAddress", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "NotificationType", "iso", "ObjectIdentity", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpNotificationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 330))
ciscoSnmpNotificationCapability.setRevisions(('2008-06-25 00:00', '2006-03-29 00:00', '2004-07-28 00:00', '2003-08-28 00:00',))
if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setLastUpdated('200806250000Z')
if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setOrganization('Cisco Systems, Inc.')
cSnmpNotifCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapCatOSV05R0501 = cSnmpNotifCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapCatOSV05R0501 = cSnmpNotifCapCatOSV05R0501.setStatus('current')
cSnmpNotifCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapVISM33 = cSnmpNotifCapVISM33.setProductRelease('Cisco VISM Release 3.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapVISM33 = cSnmpNotifCapVISM33.setStatus('current')
cSnmpNotifCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapACSWV03R000 = cSnmpNotifCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapACSWV03R000 = cSnmpNotifCapACSWV03R000.setStatus('current')
cSnmpNotifCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapc4710aceVA1R700 = cSnmpNotifCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapc4710aceVA1R700 = cSnmpNotifCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-NOTIFICATION-CAPABILITY", cSnmpNotifCapCatOSV05R0501=cSnmpNotifCapCatOSV05R0501, cSnmpNotifCapc4710aceVA1R700=cSnmpNotifCapc4710aceVA1R700, ciscoSnmpNotificationCapability=ciscoSnmpNotificationCapability, cSnmpNotifCapACSWV03R000=cSnmpNotifCapACSWV03R000, cSnmpNotifCapVISM33=cSnmpNotifCapVISM33, PYSNMP_MODULE_ID=ciscoSnmpNotificationCapability)
