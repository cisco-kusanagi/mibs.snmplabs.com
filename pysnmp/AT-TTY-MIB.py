#
# PySNMP MIB module AT-TTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-TTY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, IpAddress, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, TimeTicks, ModuleIdentity, ObjectIdentity, Gauge32, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "IpAddress", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Counter64", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
tty = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36))
tty.setRevisions(('2006-06-28 12:22',))
if mibBuilder.loadTexts: tty.setLastUpdated('200606281222Z')
if mibBuilder.loadTexts: tty.setOrganization('Allied Telesis, Inc')
ttyTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100))
loginFailureUser = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 1), DisplayString())
if mibBuilder.loadTexts: loginFailureUser.setStatus('current')
loginFailureIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 2), IpAddress())
if mibBuilder.loadTexts: loginFailureIPAddress.setStatus('current')
loginFailureAttempts = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 3), Integer32())
if mibBuilder.loadTexts: loginFailureAttempts.setStatus('current')
loginFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 11)).setObjects(("AT-TTY-MIB", "loginFailureUser"), ("AT-TTY-MIB", "loginFailureIPAddress"), ("AT-TTY-MIB", "loginFailureAttempts"))
if mibBuilder.loadTexts: loginFailureTrap.setStatus('current')
mibBuilder.exportSymbols("AT-TTY-MIB", loginFailureUser=loginFailureUser, loginFailureIPAddress=loginFailureIPAddress, tty=tty, loginFailureTrap=loginFailureTrap, loginFailureAttempts=loginFailureAttempts, ttyTraps=ttyTraps, PYSNMP_MODULE_ID=tty)
