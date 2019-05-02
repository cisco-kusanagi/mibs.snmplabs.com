#
# PySNMP MIB module ATEN-PRODUCTS-PUB-TRAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATEN-PRODUCTS-PUB-TRAP
# Produced by pysmi-0.3.4 at Wed May  1 11:30:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
public, = mibBuilder.importSymbols("ATEN-PRODUCTS-MIB", "public")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, ObjectIdentity, TimeTicks, MibIdentifier, Counter32, Bits, Unsigned32, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Counter32", "Bits", "Unsigned32", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trap = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 1, 3))
email = MibScalar((1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: email.setStatus('current')
if mibBuilder.loadTexts: email.setDescription('Name of specific(subtype) of trap in enterprise type')
log = MibScalar((1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: log.setStatus('current')
if mibBuilder.loadTexts: log.setDescription('Name of specific(subtype) of trap in enterprise type')
login = MibScalar((1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: login.setStatus('current')
if mibBuilder.loadTexts: login.setDescription("Name of specific(subtype) of 'user login event' in enterprise type")
logout = MibScalar((1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logout.setStatus('current')
if mibBuilder.loadTexts: logout.setDescription("Name of specific(subtype) of 'user logout event' in enterprise type")
mibBuilder.exportSymbols("ATEN-PRODUCTS-PUB-TRAP", login=login, logout=logout, email=email, trap=trap, log=log)
