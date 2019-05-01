#
# PySNMP MIB module AT-TTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-TTY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, ModuleIdentity, Bits, Counter32, ObjectIdentity, Integer32, Counter64, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "ModuleIdentity", "Bits", "Counter32", "ObjectIdentity", "Integer32", "Counter64", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
tty = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36))
tty.setRevisions(('2006-06-28 12:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tty.setRevisionsDescriptions(('Initial Revision',))
if mibBuilder.loadTexts: tty.setLastUpdated('200606281222Z')
if mibBuilder.loadTexts: tty.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: tty.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: tty.setDescription('This MIB file contains definitions of managed objects for the TTY module. ')
ttyTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100))
loginFailureUser = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 1), DisplayString())
if mibBuilder.loadTexts: loginFailureUser.setStatus('current')
if mibBuilder.loadTexts: loginFailureUser.setDescription('The user whose login failed')
loginFailureIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 2), IpAddress())
if mibBuilder.loadTexts: loginFailureIPAddress.setStatus('current')
if mibBuilder.loadTexts: loginFailureIPAddress.setDescription('The IP address from where the failed login attempt came')
loginFailureAttempts = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 3), Integer32())
if mibBuilder.loadTexts: loginFailureAttempts.setStatus('current')
if mibBuilder.loadTexts: loginFailureAttempts.setDescription('The number of failed logins')
loginFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 11)).setObjects(("AT-TTY-MIB", "loginFailureUser"), ("AT-TTY-MIB", "loginFailureIPAddress"), ("AT-TTY-MIB", "loginFailureAttempts"))
if mibBuilder.loadTexts: loginFailureTrap.setStatus('current')
if mibBuilder.loadTexts: loginFailureTrap.setDescription('A user has been locked out because of too many consecutive failed logins.')
mibBuilder.exportSymbols("AT-TTY-MIB", PYSNMP_MODULE_ID=tty, loginFailureAttempts=loginFailureAttempts, loginFailureIPAddress=loginFailureIPAddress, loginFailureUser=loginFailureUser, tty=tty, loginFailureTrap=loginFailureTrap, ttyTraps=ttyTraps)
