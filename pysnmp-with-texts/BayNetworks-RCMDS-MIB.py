#
# PySNMP MIB module BayNetworks-RCMDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BayNetworks-RCMDS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:42:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibIdentifier, Counter32, ObjectIdentity, IpAddress, Gauge32, TimeTicks, Integer32, ModuleIdentity, iso, NotificationType, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress", "Gauge32", "TimeTicks", "Integer32", "ModuleIdentity", "iso", "NotificationType", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfRcmdsGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfRcmdsGroup")
wfRcmds = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1))
wfRcmdsDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsDelete.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete Rcmds.')
wfRcmdsDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsDisable.setDescription('Enables or Disables Rcmds Subsystem')
wfRcmdsReservedPort = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 1023)).clone(1023)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsReservedPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsReservedPort.setDescription('Next Local reserved port available')
wfRcmdsKerberosDefaultRealmName = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsKerberosDefaultRealmName.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsKerberosDefaultRealmName.setDescription('This is the default kerberos realm name for the router')
wfRcmdsKerberosKDCName = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsKerberosKDCName.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsKerberosKDCName.setDescription('This is the default kerberos KDC name to which router sends kerberos ticket requests')
wfRcmdsRouterHostName = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRouterHostName.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRouterHostName.setDescription('This is the DNS host name for the router')
wfRcmdsKerberosHostServiceKey = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsKerberosHostServiceKey.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsKerberosHostServiceKey.setDescription('This secret equivalent of the content of V5SRVTAB file which contains the host principal keberos private key for the router. This can be manipulated only using the secure shell from the console')
wfRcmdsRlogind = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2))
wfRcmdsRlogindDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindDelete.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete')
wfRcmdsRlogindDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindDisable.setDescription('Enables or Disables Rlogind')
wfRcmdsRlogindState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRcmdsRlogindState.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindState.setDescription('State of Rlogind')
wfRcmdsRlogindMoreDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindMoreDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindMoreDisable.setDescription("Enable the 'more' feature on the Technician Interface console")
wfRcmdsRlogindPrompt = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindPrompt.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindPrompt.setDescription('Character string which will be used as the system prompt on the Technician Interface console')
wfRcmdsRlogindLoginTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindLoginTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindLoginTimeOut.setDescription('Time out in minutes to Disconnect when at the login prompt')
wfRcmdsRlogindPasswordTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindPasswordTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindPasswordTimeOut.setDescription('Timout in minutes on Password entry')
wfRcmdsRlogindCommandTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindCommandTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindCommandTimeOut.setDescription('Time out in minutes to Disconnect when at the command prompt')
wfRcmdsRlogindLoginRetries = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindLoginRetries.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindLoginRetries.setDescription('Limit # of login attempts then Disconnect')
wfRcmdsRlogindTotalLogins = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRcmdsRlogindTotalLogins.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindTotalLogins.setDescription('Total number of Rlogind TI login attempts')
wfRcmdsRlogindUserLoginErrors = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRcmdsRlogindUserLoginErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindUserLoginErrors.setDescription('Total number of FAILED User login attempts')
wfRcmdsRlogindManagerLoginErrors = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRcmdsRlogindManagerLoginErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindManagerLoginErrors.setDescription('Total number of FAILED Manager login attempts')
wfRcmdsRlogindOtherLoginErrors = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRcmdsRlogindOtherLoginErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindOtherLoginErrors.setDescription('Total number of FAILED Other login attempts')
wfRcmdsRlogindActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRcmdsRlogindActiveSessions.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindActiveSessions.setDescription('Total number of Rlogind TI Sessions')
wfRcmdsRlogindManagerAutoScript = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 15), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindManagerAutoScript.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindManagerAutoScript.setDescription('for each login.')
wfRcmdsRlogindUserAutoScript = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 16), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindUserAutoScript.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindUserAutoScript.setDescription('for each login.')
wfRcmdsRlogindUserAbortLogoutDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindUserAbortLogoutDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindUserAbortLogoutDisable.setDescription('a USER from escaping out of the User Autoscript')
wfRcmdsRlogindHistoryDepth = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindHistoryDepth.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindHistoryDepth.setDescription('TI command history table size')
wfRcmdsRlogindTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 19), Integer32().clone(543)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindTcpPort.setDescription('The TCP port on which rlogind listens. by default this is set 543, which supports kerberized rlogin')
wfRcmdsRlogindTrustedHostAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindTrustedHostAuthentication.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindTrustedHostAuthentication.setDescription('Enables/Disables Unix trusted host authentication')
wfRcmdsRlogindKerberosAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindKerberosAuthentication.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindKerberosAuthentication.setDescription('Enables/Disables Kerberos Authentication')
wfRcmdsRlogindKerberosSessionTypeAllowed = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("both", 1), ("encrypted", 2), ("unencrypted", 3), ("none", 4))).clone('both')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRlogindKerberosSessionTypeAllowed.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRlogindKerberosSessionTypeAllowed.setDescription('Encrypted/unencrypted session allowed or not')
wfRcmdsRshd = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3))
wfRcmdsRshdDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRshdDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRshdDelete.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete')
wfRcmdsRshdDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRshdDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRshdDisable.setDescription('Enables or Disables Rlogind')
wfRcmdsRshdState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRcmdsRshdState.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRshdState.setDescription('State of Rshd')
wfRcmdsRshdTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRcmdsRshdTotalSessions.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRshdTotalSessions.setDescription('Total number of Rshd command sessions executed')
wfRcmdsRshdTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 5), Integer32().clone(544)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRshdTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRshdTcpPort.setDescription('The TCP port on which rshd listens. by default this is set 544, which supports kerberized rlogin')
wfRcmdsRshdTrustedHostAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRshdTrustedHostAuthentication.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRshdTrustedHostAuthentication.setDescription('Enables/Disables Unix trusted host authentication')
wfRcmdsRshdKerberosAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRshdKerberosAuthentication.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRshdKerberosAuthentication.setDescription('Enables/Disables Kerberos Authentication')
wfRcmdsRshdKerberosSessionTypeAllowed = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("both", 1), ("encrypted", 2), ("unencrypted", 3), ("none", 4))).clone('both')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRshdKerberosSessionTypeAllowed.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRshdKerberosSessionTypeAllowed.setDescription('Encrypted/unencrypted session allowed or not')
wfRcmdsRshdRcpDefaultVolume = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 65))).clone(namedValues=NamedValues(("volume1", 1), ("volume2", 2), ("volume3", 3), ("volume4", 4), ("volume5", 5), ("volume6", 6), ("volume7", 7), ("volume8", 8), ("volume9", 9), ("volume10", 10), ("volume11", 11), ("volume12", 12), ("volume13", 13), ("volume14", 14), ("volumea", 65))).clone('volume2')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRcmdsRshdRcpDefaultVolume.setStatus('mandatory')
if mibBuilder.loadTexts: wfRcmdsRshdRcpDefaultVolume.setDescription("The file system volume number to which transferred files will be written and from which they will be retrieved. The volume number corresponds to the slot number on which the volume resides. On systems with a floppy disk, the value 65 represents volume 'A'.")
mibBuilder.exportSymbols("BayNetworks-RCMDS-MIB", wfRcmdsRlogindManagerLoginErrors=wfRcmdsRlogindManagerLoginErrors, wfRcmdsRlogindPasswordTimeOut=wfRcmdsRlogindPasswordTimeOut, wfRcmdsKerberosHostServiceKey=wfRcmdsKerberosHostServiceKey, wfRcmdsRlogindTrustedHostAuthentication=wfRcmdsRlogindTrustedHostAuthentication, wfRcmdsRshdDelete=wfRcmdsRshdDelete, wfRcmdsRlogindKerberosAuthentication=wfRcmdsRlogindKerberosAuthentication, wfRcmdsRshdKerberosAuthentication=wfRcmdsRshdKerberosAuthentication, wfRcmdsRlogindCommandTimeOut=wfRcmdsRlogindCommandTimeOut, wfRcmdsRshdTotalSessions=wfRcmdsRshdTotalSessions, wfRcmdsRlogindLoginRetries=wfRcmdsRlogindLoginRetries, wfRcmdsRshdRcpDefaultVolume=wfRcmdsRshdRcpDefaultVolume, wfRcmdsRlogindHistoryDepth=wfRcmdsRlogindHistoryDepth, wfRcmdsRlogind=wfRcmdsRlogind, wfRcmdsRlogindActiveSessions=wfRcmdsRlogindActiveSessions, wfRcmdsRlogindUserAutoScript=wfRcmdsRlogindUserAutoScript, wfRcmdsRlogindDisable=wfRcmdsRlogindDisable, wfRcmdsReservedPort=wfRcmdsReservedPort, wfRcmdsDelete=wfRcmdsDelete, wfRcmds=wfRcmds, wfRcmdsRlogindTcpPort=wfRcmdsRlogindTcpPort, wfRcmdsRlogindState=wfRcmdsRlogindState, wfRcmdsRshd=wfRcmdsRshd, wfRcmdsRlogindUserAbortLogoutDisable=wfRcmdsRlogindUserAbortLogoutDisable, wfRcmdsKerberosKDCName=wfRcmdsKerberosKDCName, wfRcmdsDisable=wfRcmdsDisable, wfRcmdsRouterHostName=wfRcmdsRouterHostName, wfRcmdsRlogindLoginTimeOut=wfRcmdsRlogindLoginTimeOut, wfRcmdsRlogindOtherLoginErrors=wfRcmdsRlogindOtherLoginErrors, wfRcmdsRlogindPrompt=wfRcmdsRlogindPrompt, wfRcmdsRlogindDelete=wfRcmdsRlogindDelete, wfRcmdsRlogindKerberosSessionTypeAllowed=wfRcmdsRlogindKerberosSessionTypeAllowed, wfRcmdsRshdTrustedHostAuthentication=wfRcmdsRshdTrustedHostAuthentication, wfRcmdsKerberosDefaultRealmName=wfRcmdsKerberosDefaultRealmName, wfRcmdsRshdTcpPort=wfRcmdsRshdTcpPort, wfRcmdsRlogindMoreDisable=wfRcmdsRlogindMoreDisable, wfRcmdsRlogindUserLoginErrors=wfRcmdsRlogindUserLoginErrors, wfRcmdsRlogindTotalLogins=wfRcmdsRlogindTotalLogins, wfRcmdsRshdDisable=wfRcmdsRshdDisable, wfRcmdsRshdKerberosSessionTypeAllowed=wfRcmdsRshdKerberosSessionTypeAllowed, wfRcmdsRshdState=wfRcmdsRshdState, wfRcmdsRlogindManagerAutoScript=wfRcmdsRlogindManagerAutoScript)
