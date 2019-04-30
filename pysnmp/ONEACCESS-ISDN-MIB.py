#
# PySNMP MIB module ONEACCESS-ISDN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-ISDN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:25:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ifAdminStatus, ifIndex, ifDescr, ifAlias, ifName, ifType, ifOperStatus = mibBuilder.importSymbols("IF-MIB", "ifAdminStatus", "ifIndex", "ifDescr", "ifAlias", "ifName", "ifType", "ifOperStatus")
oacEventText, = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventText")
oacExpIMIsdn, oacExpIMIsdnNotifications, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMIsdn", "oacExpIMIsdnNotifications", "oacMIBModules")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, IpAddress, Bits, TimeTicks, Unsigned32, Gauge32, MibIdentifier, ObjectIdentity, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Bits", "TimeTicks", "Unsigned32", "Gauge32", "MibIdentifier", "ObjectIdentity", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacIsdnMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 674))
oacIsdnMIBModule.setRevisions(('2011-10-27 00:00',))
if mibBuilder.loadTexts: oacIsdnMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacIsdnMIBModule.setOrganization(' OneAccess ')
dialDown = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 7, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialDown.setStatus('current')
dialUp = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 7, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialUp.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-ISDN-MIB", oacIsdnMIBModule=oacIsdnMIBModule, dialUp=dialUp, PYSNMP_MODULE_ID=oacIsdnMIBModule, dialDown=dialDown)
