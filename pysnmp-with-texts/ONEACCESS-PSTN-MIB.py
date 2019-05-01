#
# PySNMP MIB module ONEACCESS-PSTN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-PSTN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ifType, ifOperStatus, ifAdminStatus, ifDescr, ifIndex, ifName, ifAlias = mibBuilder.importSymbols("IF-MIB", "ifType", "ifOperStatus", "ifAdminStatus", "ifDescr", "ifIndex", "ifName", "ifAlias")
oacEventText, = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventText")
oacMIBModules, oacExpIMPstnNotifications, oacExpIMPstn = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacMIBModules", "oacExpIMPstnNotifications", "oacExpIMPstn")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter32, NotificationType, iso, Integer32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Counter64, Bits, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "NotificationType", "iso", "Integer32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Counter64", "Bits", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacPstnMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 672))
oacPstnMIBModule.setRevisions(('2011-10-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacPstnMIBModule.setRevisionsDescriptions(('This MIB module describes Pstn Management objects.',))
if mibBuilder.loadTexts: oacPstnMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacPstnMIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacPstnMIBModule.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacPstnMIBModule.setDescription('Contact updated')
dialDown = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 6, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialDown.setStatus('current')
if mibBuilder.loadTexts: dialDown.setDescription('A pstnlinkDown trap signifies that the SNMPv2 entity, acting in an agent role, has detected that the ifOperStatus object for its pstn physical link is about to enter the down state from some other state (but not from the notPresent state). This other state is indicated by the included value of ifOperStatus.')
dialUp = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 6, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialUp.setStatus('current')
if mibBuilder.loadTexts: dialUp.setDescription('A linkDown trap signifies that the SNMPv2 entity, acting in an agent role, has detected that the ifOperStatus object for for its pstn physical communication links left the down state and transitioned into some other state (but not into the notPresent state). This other state is indicated by the included value of ifOperStatus.')
mibBuilder.exportSymbols("ONEACCESS-PSTN-MIB", dialUp=dialUp, oacPstnMIBModule=oacPstnMIBModule, PYSNMP_MODULE_ID=oacPstnMIBModule, dialDown=dialDown)
