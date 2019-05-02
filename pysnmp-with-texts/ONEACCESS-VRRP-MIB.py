#
# PySNMP MIB module ONEACCESS-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-VRRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
oacEventText, = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventText")
oacExpIMVrrpNotifications, oacExpIMIpVrrp, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMVrrpNotifications", "oacExpIMIpVrrp", "oacMIBModules")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, Gauge32, IpAddress, Integer32, Unsigned32, iso, Counter32, TimeTicks, ObjectIdentity, ModuleIdentity, Bits, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "IpAddress", "Integer32", "Unsigned32", "iso", "Counter32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Bits", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacVrrpMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 670))
oacVrrpMIBModule.setRevisions(('2011-10-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacVrrpMIBModule.setRevisionsDescriptions(('This MIB module describes IP VRRP Management objects.',))
if mibBuilder.loadTexts: oacVrrpMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacVrrpMIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacVrrpMIBModule.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacVrrpMIBModule.setDescription('Contact updated')
vrrpTrapNewBackup = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 5, 1, 1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"))
if mibBuilder.loadTexts: vrrpTrapNewBackup.setStatus('current')
if mibBuilder.loadTexts: vrrpTrapNewBackup.setDescription("The newBackup trap indicates that the sending agent has transitioned to 'Backup' state.")
mibBuilder.exportSymbols("ONEACCESS-VRRP-MIB", vrrpTrapNewBackup=vrrpTrapNewBackup, PYSNMP_MODULE_ID=oacVrrpMIBModule, oacVrrpMIBModule=oacVrrpMIBModule)
