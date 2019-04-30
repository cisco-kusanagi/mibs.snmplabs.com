#
# PySNMP MIB module ATEN-PRODUCTS-PUB-TRAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATEN-PRODUCTS-PUB-TRAP
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
public, = mibBuilder.importSymbols("ATEN-PRODUCTS-MIB", "public")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, NotificationType, Counter64, Counter32, Integer32, IpAddress, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "NotificationType", "Counter64", "Counter32", "Integer32", "IpAddress", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trap = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 1, 3))
email = MibScalar((1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: email.setStatus('current')
log = MibScalar((1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: log.setStatus('current')
login = MibScalar((1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: login.setStatus('current')
logout = MibScalar((1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logout.setStatus('current')
mibBuilder.exportSymbols("ATEN-PRODUCTS-PUB-TRAP", trap=trap, log=log, email=email, login=login, logout=logout)
