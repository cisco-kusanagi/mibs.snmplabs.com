#
# PySNMP MIB module CISCO-AAA-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AAA-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, NotificationType, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter64, IpAddress, Counter32, Bits, Unsigned32, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter64", "IpAddress", "Counter32", "Bits", "Unsigned32", "MibIdentifier", "Integer32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoAAAClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 158))
ciscoAAAClientMIB.setRevisions(('2001-11-19 00:00', '2001-05-10 00:00',))
if mibBuilder.loadTexts: ciscoAAAClientMIB.setLastUpdated('200111190000Z')
if mibBuilder.loadTexts: ciscoAAAClientMIB.setOrganization('Cisco Systems, Inc.')
class SessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("telnet", 1), ("console", 2), ("http", 3))

class AuthenMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("tacacs", 1), ("radius", 2), ("kerberos", 3), ("local", 4))

class LoginMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("login", 1), ("enable", 2))

cacMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1))
cacPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1))
cacLoginConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2))
cacPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1), )
if mibBuilder.loadTexts: cacPriorityTable.setStatus('current')
cacPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-AAA-CLIENT-MIB", "cacSession"), (0, "CISCO-AAA-CLIENT-MIB", "cacAuthen"), (0, "CISCO-AAA-CLIENT-MIB", "cacLoginMode"))
if mibBuilder.loadTexts: cacPriorityEntry.setStatus('current')
cacSession = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 1), SessionType())
if mibBuilder.loadTexts: cacSession.setStatus('current')
cacAuthen = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 2), AuthenMethod())
if mibBuilder.loadTexts: cacAuthen.setStatus('current')
cacLoginMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 3), LoginMode())
if mibBuilder.loadTexts: cacLoginMode.setStatus('current')
cacEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacEnable.setStatus('current')
cacPriorityNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacPriorityNumber.setStatus('current')
cacPrimaryMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacPrimaryMethod.setStatus('current')
cacLoginConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1), )
if mibBuilder.loadTexts: cacLoginConfigTable.setStatus('current')
cacLoginConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-AAA-CLIENT-MIB", "cacLoginMode"), (0, "CISCO-AAA-CLIENT-MIB", "cacSession"))
if mibBuilder.loadTexts: cacLoginConfigEntry.setStatus('current')
cacMaxLoginAttempt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 10), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacMaxLoginAttempt.setStatus('current')
cacLockoutPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 600), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacLockoutPeriod.setStatus('deprecated')
cacLockoutPeriodExt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 43200), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacLockoutPeriodExt.setStatus('current')
cacMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 2))
cacMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3))
cacMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1))
cacMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2))
cacMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1, 1)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacPriorityGroup"), ("CISCO-AAA-CLIENT-MIB", "cacLoginConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacMIBCompliance = cacMIBCompliance.setStatus('deprecated')
cacMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1, 2)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacPriorityGroup"), ("CISCO-AAA-CLIENT-MIB", "cacLoginConfigGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacMIBCompliance2 = cacMIBCompliance2.setStatus('current')
cacPriorityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 1)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacEnable"), ("CISCO-AAA-CLIENT-MIB", "cacPriorityNumber"), ("CISCO-AAA-CLIENT-MIB", "cacPrimaryMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacPriorityGroup = cacPriorityGroup.setStatus('current')
cacLoginConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 2)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacMaxLoginAttempt"), ("CISCO-AAA-CLIENT-MIB", "cacLockoutPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLoginConfigGroup = cacLoginConfigGroup.setStatus('deprecated')
cacLoginConfigGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 3)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacMaxLoginAttempt"), ("CISCO-AAA-CLIENT-MIB", "cacLockoutPeriodExt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLoginConfigGroupRev1 = cacLoginConfigGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-CLIENT-MIB", cacLoginMode=cacLoginMode, ciscoAAAClientMIB=ciscoAAAClientMIB, cacPriorityTable=cacPriorityTable, cacPrimaryMethod=cacPrimaryMethod, cacMIBNotifications=cacMIBNotifications, cacMIBCompliances=cacMIBCompliances, cacMaxLoginAttempt=cacMaxLoginAttempt, cacEnable=cacEnable, cacLoginConfigTable=cacLoginConfigTable, cacMIBObjects=cacMIBObjects, cacLoginConfig=cacLoginConfig, cacLoginConfigGroupRev1=cacLoginConfigGroupRev1, cacLoginConfigGroup=cacLoginConfigGroup, AuthenMethod=AuthenMethod, cacLockoutPeriod=cacLockoutPeriod, SessionType=SessionType, cacAuthen=cacAuthen, cacPriorityEntry=cacPriorityEntry, cacSession=cacSession, PYSNMP_MODULE_ID=ciscoAAAClientMIB, cacMIBCompliance2=cacMIBCompliance2, cacPriorityGroup=cacPriorityGroup, cacLoginConfigEntry=cacLoginConfigEntry, cacMIBCompliance=cacMIBCompliance, cacMIBGroups=cacMIBGroups, cacLockoutPeriodExt=cacLockoutPeriodExt, cacPriorityNumber=cacPriorityNumber, cacMIBConformance=cacMIBConformance, LoginMode=LoginMode, cacPriority=cacPriority)
