#
# PySNMP MIB module TPLINK-HTTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-HTTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, ObjectIdentity, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, NotificationType, Gauge32, Counter64, Integer32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "ObjectIdentity", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "NotificationType", "Gauge32", "Counter64", "Integer32", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkHttp = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 51))
tplinkHttp.setRevisions(('2015-01-21 10:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkHttp.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkHttp.setLastUpdated('201501211030Z')
if mibBuilder.loadTexts: tplinkHttp.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkHttp.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkHttp.setDescription('Private MIB for HTTP configuration.')
tplinkHttpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 51, 1))
tplinkHttpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 51, 2))
httpEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: httpEnable.setStatus('current')
if mibBuilder.loadTexts: httpEnable.setDescription('0. disable 1. enable')
httpSessionTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: httpSessionTimeOut.setStatus('current')
if mibBuilder.loadTexts: httpSessionTimeOut.setDescription('HTTP session timeout in minutes.')
httpUserLimitEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: httpUserLimitEnable.setStatus('current')
if mibBuilder.loadTexts: httpUserLimitEnable.setDescription('0. disable 1.enable')
httpUserLimitMaxAdminNum = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: httpUserLimitMaxAdminNum.setStatus('current')
if mibBuilder.loadTexts: httpUserLimitMaxAdminNum.setDescription('The max num of admin users. You should enable HTTP user number limiting before setting this object.')
httpUserLimitMaxGuestNum = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: httpUserLimitMaxGuestNum.setStatus('current')
if mibBuilder.loadTexts: httpUserLimitMaxGuestNum.setDescription('The max num of guest users. You should enable HTTP user number limiting before setting this object.')
mibBuilder.exportSymbols("TPLINK-HTTP-MIB", tplinkHttpMIBNotifications=tplinkHttpMIBNotifications, httpUserLimitMaxGuestNum=httpUserLimitMaxGuestNum, tplinkHttpMIBObjects=tplinkHttpMIBObjects, tplinkHttp=tplinkHttp, httpSessionTimeOut=httpSessionTimeOut, httpUserLimitEnable=httpUserLimitEnable, httpUserLimitMaxAdminNum=httpUserLimitMaxAdminNum, httpEnable=httpEnable, PYSNMP_MODULE_ID=tplinkHttp)
