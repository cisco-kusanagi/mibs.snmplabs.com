#
# PySNMP MIB module CISCO-AAA-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AAA-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Counter64, Integer32, iso, IpAddress, NotificationType, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Counter64", "Integer32", "iso", "IpAddress", "NotificationType", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "ObjectIdentity", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoAAAClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 158))
ciscoAAAClientMIB.setRevisions(('2001-11-19 00:00', '2001-05-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAAAClientMIB.setRevisionsDescriptions(('Deprecate object cacLockoutPeriod and add a new object cacLockoutPeriodExt. ', 'Initial version ',))
if mibBuilder.loadTexts: ciscoAAAClientMIB.setLastUpdated('200111190000Z')
if mibBuilder.loadTexts: ciscoAAAClientMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAAAClientMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoAAAClientMIB.setDescription('This MIB module provides data for authentication method priority based on Authentication, Authorization, Accounting (AAA) protocols. References: The TACACS+ Protocol Version 1.78, Internet Draft RFC 1411 Telnet Authentication: Kerberos Version 4. RFC 1964 The Kerberos Version 5 GSS-API Mechanism. ')
class SessionType(TextualConvention, Integer32):
    description = 'Represents a session type. telnet(1) indicates telnet session. console(2) indicates console session. http(3) indicates http session. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("telnet", 1), ("console", 2), ("http", 3))

class AuthenMethod(TextualConvention, Integer32):
    description = 'Represents authentication method. tacacs(1) indicates that TACACS method is used for authentication. radius(2) indicates that RADIUS method is used for authentication. kerberos(3) indicates that KERBEROS method is used for authentication. local(4) indicates that local password is used for authentication. Which password is used depend on what login mode users specified. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("tacacs", 1), ("radius", 2), ("kerberos", 3), ("local", 4))

class LoginMode(TextualConvention, Integer32):
    description = 'Represents login mode. login(1) indicates the normal mode. enable(2) indicates the privileged mode. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("login", 1), ("enable", 2))

cacMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1))
cacPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1))
cacLoginConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2))
cacPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1), )
if mibBuilder.loadTexts: cacPriorityTable.setStatus('current')
if mibBuilder.loadTexts: cacPriorityTable.setDescription('This table contains entries for AAA authentication methods configured in the system. At startup, agent set up all the entries of the table. All authentication methods will be disabled except local authentication will be enabled for each session type and login mode. Users later can enable/disable a specific authentication method through cacEnable object. The following table describes the startup state of each authentication method and session type in normal login mode and enable login mode. AuthenMethod Console Session Telnet Session Http Session ------------ ---------------- ---------------- ------------ tacacs disabled disabled disabled radius disabled disabled disabled kerberos disabled disabled disabled local enabled(*) enabled(*) enabled(*) (*) denotes primary method. ')
cacPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-AAA-CLIENT-MIB", "cacSession"), (0, "CISCO-AAA-CLIENT-MIB", "cacAuthen"), (0, "CISCO-AAA-CLIENT-MIB", "cacLoginMode"))
if mibBuilder.loadTexts: cacPriorityEntry.setStatus('current')
if mibBuilder.loadTexts: cacPriorityEntry.setDescription('An entry containing the priority number of an authentication method used in a session. ')
cacSession = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 1), SessionType())
if mibBuilder.loadTexts: cacSession.setStatus('current')
if mibBuilder.loadTexts: cacSession.setDescription('This is the session type used to connect to the network device. ')
cacAuthen = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 2), AuthenMethod())
if mibBuilder.loadTexts: cacAuthen.setStatus('current')
if mibBuilder.loadTexts: cacAuthen.setDescription('This is the authentication method used to authenticate users. ')
cacLoginMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 3), LoginMode())
if mibBuilder.loadTexts: cacLoginMode.setStatus('current')
if mibBuilder.loadTexts: cacLoginMode.setDescription('This is the login mode user used to login to the network device. ')
cacEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacEnable.setStatus('current')
if mibBuilder.loadTexts: cacEnable.setDescription('It indicates whether the authentication method denoted by cacAuthen is enabled or not. When this object is true(1), the authentication method denoted by cacAuthen is enabled. When this object is false(2), the authentication method denoted by cacAuthen is disabled. If the value of cacAuthen is local, the value of this object cannot be set to false(2). ')
cacPriorityNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacPriorityNumber.setStatus('current')
if mibBuilder.loadTexts: cacPriorityNumber.setDescription('This is the priority number of an authentication method to be used in user authentication for a session. This value is automatically assigned and reflects the relative priority of the authentication method denoted by cacAuthen with respected to already configured authentication methods. It is assigned in the order in which the authentication method is enabled by the user through cacEnable. The higher value has the higher priority. This object is used to determine the fallback order in case the primary authentication method indicated by cacPrimaryMethod failed. If the authentication method denoted by cacAuthen is disabled for the type of session denoted by cacSession, the value of this object is equal to 0. ')
cacPrimaryMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacPrimaryMethod.setStatus('current')
if mibBuilder.loadTexts: cacPrimaryMethod.setDescription('It indicates whether the authentication method denoted by cacAuthen is the primary (first one to be tried) method when there are multiple authentication method configured. Setting this object to true(1) will make the authentication method denoted by cacAuthen to be the primary authentication method for the session denoted by cacSession. The previously configured primary method will be changed to false(2). Setting this object to false(2) is not allowed. ')
cacLoginConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1), )
if mibBuilder.loadTexts: cacLoginConfigTable.setStatus('current')
if mibBuilder.loadTexts: cacLoginConfigTable.setDescription('A table that contains login configuration which is associated with this system. ')
cacLoginConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-AAA-CLIENT-MIB", "cacLoginMode"), (0, "CISCO-AAA-CLIENT-MIB", "cacSession"))
if mibBuilder.loadTexts: cacLoginConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cacLoginConfigEntry.setDescription('An entry containing the configuration of the login. ')
cacMaxLoginAttempt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 10), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacMaxLoginAttempt.setStatus('current')
if mibBuilder.loadTexts: cacMaxLoginAttempt.setDescription('Indicates the maximum number of login attempts allowed. Setting this variable to 0 will disable the attempt limit checking. If the login session type does not support this attempt limit checking, the value of this object can only be set to 0. ')
cacLockoutPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 600), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacLockoutPeriod.setStatus('deprecated')
if mibBuilder.loadTexts: cacLockoutPeriod.setDescription('Indicates the lockout period after the maximum number of login attempt is met. For console, the console input will be frozen during this period. For remote logins, the connection will be closed and any subsequent access from that station will be closed during the lockout time. Setting this variable to 0 will disable the lockout. If the login session type does not support this lockout period, the value of this object can only be set to 0. If the lockout period is greater than the maximum value reportable by this object then this object should report its maximum value (600) and cacLockoutPeriodExt must be used to report the lockout period. ')
cacLockoutPeriodExt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 43200), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacLockoutPeriodExt.setStatus('current')
if mibBuilder.loadTexts: cacLockoutPeriodExt.setDescription('Specifies the lockout period after the maximum number of login attempt is met. For console, the console input will be frozen during this period. For remote logins, the connection will be closed and any subsequent access from that station will be closed during the lockout time. Setting this variable to 0 will disable the lockout. If the login session type does not support this lockout period, the value of this object can only be set to 0. ')
cacMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 2))
cacMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3))
cacMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1))
cacMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2))
cacMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1, 1)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacPriorityGroup"), ("CISCO-AAA-CLIENT-MIB", "cacLoginConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacMIBCompliance = cacMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cacMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO AAA Client MIB')
cacMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1, 2)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacPriorityGroup"), ("CISCO-AAA-CLIENT-MIB", "cacLoginConfigGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacMIBCompliance2 = cacMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: cacMIBCompliance2.setDescription('The compliance statement for entities which implement the CISCO AAA Client MIB')
cacPriorityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 1)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacEnable"), ("CISCO-AAA-CLIENT-MIB", "cacPriorityNumber"), ("CISCO-AAA-CLIENT-MIB", "cacPrimaryMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacPriorityGroup = cacPriorityGroup.setStatus('current')
if mibBuilder.loadTexts: cacPriorityGroup.setDescription('A collection of objects providing the AAA client priority information. ')
cacLoginConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 2)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacMaxLoginAttempt"), ("CISCO-AAA-CLIENT-MIB", "cacLockoutPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLoginConfigGroup = cacLoginConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cacLoginConfigGroup.setDescription('A collection of objects providing the AAA client login configuration. ')
cacLoginConfigGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 3)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacMaxLoginAttempt"), ("CISCO-AAA-CLIENT-MIB", "cacLockoutPeriodExt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLoginConfigGroupRev1 = cacLoginConfigGroupRev1.setStatus('current')
if mibBuilder.loadTexts: cacLoginConfigGroupRev1.setDescription('A collection of objects providing the AAA client login configuration. ')
mibBuilder.exportSymbols("CISCO-AAA-CLIENT-MIB", cacLoginConfig=cacLoginConfig, cacPriorityGroup=cacPriorityGroup, cacPriorityNumber=cacPriorityNumber, cacSession=cacSession, cacLoginConfigEntry=cacLoginConfigEntry, cacMaxLoginAttempt=cacMaxLoginAttempt, cacMIBNotifications=cacMIBNotifications, cacEnable=cacEnable, cacMIBObjects=cacMIBObjects, cacMIBCompliance=cacMIBCompliance, cacLoginConfigGroupRev1=cacLoginConfigGroupRev1, cacLockoutPeriod=cacLockoutPeriod, cacLoginConfigGroup=cacLoginConfigGroup, cacPriorityEntry=cacPriorityEntry, ciscoAAAClientMIB=ciscoAAAClientMIB, SessionType=SessionType, cacLockoutPeriodExt=cacLockoutPeriodExt, AuthenMethod=AuthenMethod, PYSNMP_MODULE_ID=ciscoAAAClientMIB, cacLoginConfigTable=cacLoginConfigTable, cacMIBCompliances=cacMIBCompliances, cacMIBCompliance2=cacMIBCompliance2, cacPrimaryMethod=cacPrimaryMethod, LoginMode=LoginMode, cacPriority=cacPriority, cacAuthen=cacAuthen, cacPriorityTable=cacPriorityTable, cacMIBGroups=cacMIBGroups, cacMIBConformance=cacMIBConformance, cacLoginMode=cacLoginMode)
