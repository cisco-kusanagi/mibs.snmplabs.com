#
# PySNMP MIB module ONEACCESS-ISDN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-ISDN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifAlias, ifName, ifType, ifAdminStatus, ifDescr, ifOperStatus, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifAlias", "ifName", "ifType", "ifAdminStatus", "ifDescr", "ifOperStatus", "ifIndex")
oacEventText, = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventText")
oacExpIMIsdn, oacExpIMIsdnNotifications, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMIsdn", "oacExpIMIsdnNotifications", "oacMIBModules")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, IpAddress, Gauge32, ModuleIdentity, MibIdentifier, Bits, Counter64, iso, ObjectIdentity, Counter32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "IpAddress", "Gauge32", "ModuleIdentity", "MibIdentifier", "Bits", "Counter64", "iso", "ObjectIdentity", "Counter32", "NotificationType", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacIsdnMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 674))
oacIsdnMIBModule.setRevisions(('2011-10-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacIsdnMIBModule.setRevisionsDescriptions(('This MIB module describes IP Isdn Management objects.',))
if mibBuilder.loadTexts: oacIsdnMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacIsdnMIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacIsdnMIBModule.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacIsdnMIBModule.setDescription('Contact updated')
dialDown = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 7, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialDown.setStatus('current')
if mibBuilder.loadTexts: dialDown.setDescription('A IsdnlinkDown trap signifies that the SNMPv2 entity, acting in an agent role, has detected that the ifOperStatus object for its Isdn physical link is about to enter the down state from some other state (but not from the notPresent state). This other state is indicated by the included value of ifOperStatus.')
dialUp = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 7, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialUp.setStatus('current')
if mibBuilder.loadTexts: dialUp.setDescription('A linkDown trap signifies that the SNMPv2 entity, acting in an agent role, has detected that the ifOperStatus object for for its Isdn physical communication links left the down state and transitioned into some other state (but not into the notPresent state). This other state is indicated by the included value of ifOperStatus.')
mibBuilder.exportSymbols("ONEACCESS-ISDN-MIB", dialUp=dialUp, dialDown=dialDown, PYSNMP_MODULE_ID=oacIsdnMIBModule, oacIsdnMIBModule=oacIsdnMIBModule)
