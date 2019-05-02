#
# PySNMP MIB module A3COM-HUAWEI-WEB-AUTHENTICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-WEB-AUTHENTICATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:07:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifDescr, = mibBuilder.importSymbols("IF-MIB", "ifDescr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, ObjectIdentity, Gauge32, Unsigned32, ModuleIdentity, Bits, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ObjectIdentity", "Gauge32", "Unsigned32", "ModuleIdentity", "Bits", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Integer32", "IpAddress")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
h3cWebAuthentication = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93))
h3cWebAuthentication.setRevisions(('2008-06-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cWebAuthentication.setRevisionsDescriptions(('The initial version of h3cWebAuthenticationMIB',))
if mibBuilder.loadTexts: h3cWebAuthentication.setLastUpdated('200806250000Z')
if mibBuilder.loadTexts: h3cWebAuthentication.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: h3cWebAuthentication.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: h3cWebAuthentication.setDescription('The MIB module is used for web authentication to send traps.')
h3cWaTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 1))
h3cWaVlanID = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cWaVlanID.setStatus('current')
if mibBuilder.loadTexts: h3cWaVlanID.setDescription('The Vlan ID associate with the port and the MAC address.')
h3cWaReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("globalNumberMax", 1), ("configNumberMax", 2), ("portNumberMax", 3), ("invalidUsername", 4), ("authFail", 5), ("setACLFail", 6), ("changeVlanFail", 7), ("other", 8), ("onlineOverTime", 9), ("noTransferData", 10), ("cutOperation", 11), ("portDisabled", 12), ("portDown", 13), ("userLogout", 14), ("vlanChanged", 15), ("vlanDelted", 16)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cWaReasonCode.setStatus('current')
if mibBuilder.loadTexts: h3cWaReasonCode.setDescription('The code indicates the reason for the action of this trap. globalNumberMax: The global number of connections is up to max. configNumberMax: The global number of connections is up to configured max value. portNumberMax: The interface number of connections is up to max. invalidUsername: The username or password is too long or username is empty. authFail: Wrong username or password. setACLFail: Failed to set ACL. changeVlanFail: Failed to set VLAN. other: Other reasons. onlineOverTime: The online time is over the max value. noTransferData: There was no data flow for the connection. cutOperation: There was a cut operation. portDisabled: Web authentication was disabled on interface. portDown: The interface turned down. userLogout: The client required to logout. vlanChanged: The interface VLAN value was changed. vlanDelted: The interface VLAN was deleted.')
h3cWaActionCode = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cWaActionCode.setStatus('current')
if mibBuilder.loadTexts: h3cWaActionCode.setDescription('The code indicates the system action. enabled: Web authentication turns enabled. disabled: Web authentication turns disabled.')
h3cWaClientMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 1, 4), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cWaClientMacAddr.setStatus('current')
if mibBuilder.loadTexts: h3cWaClientMacAddr.setDescription('The MAC address of the client.')
h3cWaTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2))
h3cWaTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2, 0))
h3cWaClientLogon = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2, 0, 1)).setObjects(("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaClientMacAddr"), ("IF-MIB", "ifDescr"), ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaVlanID"))
if mibBuilder.loadTexts: h3cWaClientLogon.setStatus('current')
if mibBuilder.loadTexts: h3cWaClientLogon.setDescription('It is generated when a client succeeded to logon.')
h3cWaClientLogonFail = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2, 0, 2)).setObjects(("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaClientMacAddr"), ("IF-MIB", "ifDescr"), ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaVlanID"), ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaReasonCode"))
if mibBuilder.loadTexts: h3cWaClientLogonFail.setStatus('current')
if mibBuilder.loadTexts: h3cWaClientLogonFail.setDescription('It is generated when a client failed to logon, the h3cWaReasonCode shows the failure reason.')
h3cWaClientLogout = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2, 0, 3)).setObjects(("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaClientMacAddr"), ("IF-MIB", "ifDescr"), ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaVlanID"), ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaReasonCode"))
if mibBuilder.loadTexts: h3cWaClientLogout.setStatus('current')
if mibBuilder.loadTexts: h3cWaClientLogout.setDescription('It is generated when a client logout, the h3cWaReasonCode shows the logout reason.')
h3cWaSysAction = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2, 0, 4)).setObjects(("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaActionCode"))
if mibBuilder.loadTexts: h3cWaSysAction.setStatus('current')
if mibBuilder.loadTexts: h3cWaSysAction.setDescription('It is generated when a system action was occurred, the h3cWaActionCode shows the action information.')
mibBuilder.exportSymbols("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", h3cWaClientLogonFail=h3cWaClientLogonFail, h3cWebAuthentication=h3cWebAuthentication, h3cWaActionCode=h3cWaActionCode, h3cWaTrapPrefix=h3cWaTrapPrefix, h3cWaTrap=h3cWaTrap, h3cWaSysAction=h3cWaSysAction, h3cWaClientLogon=h3cWaClientLogon, h3cWaVlanID=h3cWaVlanID, PYSNMP_MODULE_ID=h3cWebAuthentication, h3cWaClientMacAddr=h3cWaClientMacAddr, h3cWaReasonCode=h3cWaReasonCode, h3cWaClientLogout=h3cWaClientLogout, h3cWaTrapObjects=h3cWaTrapObjects)
