#
# PySNMP MIB module ONEACCESS-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-VRRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:25:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
oacEventText, = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventText")
oacMIBModules, oacExpIMIpVrrp, oacExpIMVrrpNotifications = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacMIBModules", "oacExpIMIpVrrp", "oacExpIMVrrpNotifications")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, ObjectIdentity, Integer32, TimeTicks, Bits, iso, Gauge32, Counter32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "ObjectIdentity", "Integer32", "TimeTicks", "Bits", "iso", "Gauge32", "Counter32", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacVrrpMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 670))
oacVrrpMIBModule.setRevisions(('2011-10-27 00:00',))
if mibBuilder.loadTexts: oacVrrpMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacVrrpMIBModule.setOrganization(' OneAccess ')
vrrpTrapNewBackup = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 5, 1, 1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"))
if mibBuilder.loadTexts: vrrpTrapNewBackup.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-VRRP-MIB", PYSNMP_MODULE_ID=oacVrrpMIBModule, vrrpTrapNewBackup=vrrpTrapNewBackup, oacVrrpMIBModule=oacVrrpMIBModule)
