#
# PySNMP MIB module ONEACCESS-PSTN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-PSTN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:25:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifType, ifDescr, ifName, ifAlias, ifAdminStatus, ifIndex, ifOperStatus = mibBuilder.importSymbols("IF-MIB", "ifType", "ifDescr", "ifName", "ifAlias", "ifAdminStatus", "ifIndex", "ifOperStatus")
oacEventText, = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventText")
oacMIBModules, oacExpIMPstnNotifications, oacExpIMPstn = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacMIBModules", "oacExpIMPstnNotifications", "oacExpIMPstn")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, iso, Bits, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, ObjectIdentity, NotificationType, MibIdentifier, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "iso", "Bits", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "ObjectIdentity", "NotificationType", "MibIdentifier", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacPstnMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 672))
oacPstnMIBModule.setRevisions(('2011-10-27 00:00',))
if mibBuilder.loadTexts: oacPstnMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacPstnMIBModule.setOrganization(' OneAccess ')
dialDown = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 6, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialDown.setStatus('current')
dialUp = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 6, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialUp.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-PSTN-MIB", dialDown=dialDown, PYSNMP_MODULE_ID=oacPstnMIBModule, oacPstnMIBModule=oacPstnMIBModule, dialUp=dialUp)
