#
# PySNMP MIB module ASCEND-MIBLSMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBLSMS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, Bits, iso, Counter32, Counter64, Gauge32, ModuleIdentity, ObjectIdentity, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Bits", "iso", "Counter32", "Counter64", "Gauge32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

miblsmsProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 150))
miblsmsProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 150, 1), )
if mibBuilder.loadTexts: miblsmsProfileTable.setStatus('mandatory')
miblsmsProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1), ).setIndexNames((0, "ASCEND-MIBLSMS-MIB", "lsmsProfile-Index-o"))
if mibBuilder.loadTexts: miblsmsProfileEntry.setStatus('mandatory')
lsmsProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 1), Integer32()).setLabel("lsmsProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: lsmsProfile_Index_o.setStatus('mandatory')
lsmsProfile_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("lsmsProfile-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsmsProfile_Active.setStatus('mandatory')
lsmsProfile_LsmsIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 3), IpAddress()).setLabel("lsmsProfile-LsmsIpAddr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsmsProfile_LsmsIpAddr.setStatus('mandatory')
lsmsProfile_NocGatewayIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 4), IpAddress()).setLabel("lsmsProfile-NocGatewayIpAddr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsmsProfile_NocGatewayIpAddr.setStatus('mandatory')
lsmsProfile_Spi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 5), DisplayString()).setLabel("lsmsProfile-Spi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsmsProfile_Spi.setStatus('mandatory')
lsmsProfile_PresharedKey = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 6), DisplayString()).setLabel("lsmsProfile-PresharedKey").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsmsProfile_PresharedKey.setStatus('mandatory')
lsmsProfile_AllowInsecure = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("lsmsProfile-AllowInsecure").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsmsProfile_AllowInsecure.setStatus('mandatory')
lsmsProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("lsmsProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsmsProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBLSMS-MIB", lsmsProfile_LsmsIpAddr=lsmsProfile_LsmsIpAddr, lsmsProfile_AllowInsecure=lsmsProfile_AllowInsecure, miblsmsProfileEntry=miblsmsProfileEntry, lsmsProfile_NocGatewayIpAddr=lsmsProfile_NocGatewayIpAddr, DisplayString=DisplayString, lsmsProfile_Active=lsmsProfile_Active, lsmsProfile_PresharedKey=lsmsProfile_PresharedKey, lsmsProfile_Action_o=lsmsProfile_Action_o, lsmsProfile_Spi=lsmsProfile_Spi, lsmsProfile_Index_o=lsmsProfile_Index_o, miblsmsProfile=miblsmsProfile, miblsmsProfileTable=miblsmsProfileTable)
