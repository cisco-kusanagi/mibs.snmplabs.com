#
# PySNMP MIB module ASCEND-MIBIPSECSPD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBIPSECSPD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, Counter32, iso, IpAddress, Integer32, ModuleIdentity, Unsigned32, Counter64, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "Counter32", "iso", "IpAddress", "Integer32", "ModuleIdentity", "Unsigned32", "Counter64", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibmibProfIpsecSpd = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 168))
mibmibProfIpsecSpdTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 168, 1), )
if mibBuilder.loadTexts: mibmibProfIpsecSpdTable.setStatus('mandatory')
mibmibProfIpsecSpdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 168, 1, 1), ).setIndexNames((0, "ASCEND-MIBIPSECSPD-MIB", "mibProfIpsecSpd-SpdName"))
if mibBuilder.loadTexts: mibmibProfIpsecSpdEntry.setStatus('mandatory')
mibProfIpsecSpd_SpdName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 168, 1, 1, 1), DisplayString()).setLabel("mibProfIpsecSpd-SpdName").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfIpsecSpd_SpdName.setStatus('mandatory')
mibProfIpsecSpd_DefaultFilter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 168, 1, 1, 2), DisplayString()).setLabel("mibProfIpsecSpd-DefaultFilter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecSpd_DefaultFilter.setStatus('mandatory')
mibProfIpsecSpd_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 168, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfIpsecSpd-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecSpd_Action_o.setStatus('mandatory')
mibmibProfIpsecSpd_PolicyTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 168, 2), ).setLabel("mibmibProfIpsecSpd-PolicyTable")
if mibBuilder.loadTexts: mibmibProfIpsecSpd_PolicyTable.setStatus('mandatory')
mibmibProfIpsecSpd_PolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 168, 2, 1), ).setLabel("mibmibProfIpsecSpd-PolicyEntry").setIndexNames((0, "ASCEND-MIBIPSECSPD-MIB", "mibProfIpsecSpd-Policy-SpdName"), (0, "ASCEND-MIBIPSECSPD-MIB", "mibProfIpsecSpd-Policy-Index-o"))
if mibBuilder.loadTexts: mibmibProfIpsecSpd_PolicyEntry.setStatus('mandatory')
mibProfIpsecSpd_Policy_SpdName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 168, 2, 1, 1), DisplayString()).setLabel("mibProfIpsecSpd-Policy-SpdName").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfIpsecSpd_Policy_SpdName.setStatus('mandatory')
mibProfIpsecSpd_Policy_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 168, 2, 1, 2), Integer32()).setLabel("mibProfIpsecSpd-Policy-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfIpsecSpd_Policy_Index_o.setStatus('mandatory')
mibProfIpsecSpd_Policy = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 168, 2, 1, 3), DisplayString()).setLabel("mibProfIpsecSpd-Policy").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecSpd_Policy.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBIPSECSPD-MIB", mibmibProfIpsecSpdTable=mibmibProfIpsecSpdTable, mibProfIpsecSpd_SpdName=mibProfIpsecSpd_SpdName, mibmibProfIpsecSpd=mibmibProfIpsecSpd, mibProfIpsecSpd_Policy=mibProfIpsecSpd_Policy, mibmibProfIpsecSpd_PolicyEntry=mibmibProfIpsecSpd_PolicyEntry, mibProfIpsecSpd_Policy_Index_o=mibProfIpsecSpd_Policy_Index_o, mibmibProfIpsecSpdEntry=mibmibProfIpsecSpdEntry, mibProfIpsecSpd_Policy_SpdName=mibProfIpsecSpd_Policy_SpdName, mibmibProfIpsecSpd_PolicyTable=mibmibProfIpsecSpd_PolicyTable, mibProfIpsecSpd_Action_o=mibProfIpsecSpd_Action_o, DisplayString=DisplayString, mibProfIpsecSpd_DefaultFilter=mibProfIpsecSpd_DefaultFilter)
