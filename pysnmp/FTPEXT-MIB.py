#
# PySNMP MIB module FTPEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FTPEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:02:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ftpExt, = mibBuilder.importSymbols("APENT-MIB", "ftpExt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, TimeTicks, Counter64, ObjectIdentity, Bits, iso, IpAddress, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "TimeTicks", "Counter64", "ObjectIdentity", "Bits", "iso", "IpAddress", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ftpExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 30, 1))
if mibBuilder.loadTexts: ftpExtMib.setLastUpdated('9801282000Z')
if mibBuilder.loadTexts: ftpExtMib.setOrganization('ArrowPoint Communications Inc.')
apFtpTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 30, 2), )
if mibBuilder.loadTexts: apFtpTable.setStatus('current')
apFtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1), ).setIndexNames((0, "FTPEXT-MIB", "apFtpRecordName"))
if mibBuilder.loadTexts: apFtpEntry.setStatus('current')
apFtpRecordName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apFtpRecordName.setStatus('current')
apFtpIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apFtpIpAddress.setStatus('current')
apFtpUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apFtpUserName.setStatus('current')
apFtpPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apFtpPassword.setStatus('current')
apFtpEncryptedPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apFtpEncryptedPassword.setStatus('current')
apFtpBaseDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apFtpBaseDirectory.setStatus('current')
apFtpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 30, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apFtpStatus.setStatus('current')
mibBuilder.exportSymbols("FTPEXT-MIB", apFtpBaseDirectory=apFtpBaseDirectory, apFtpRecordName=apFtpRecordName, apFtpIpAddress=apFtpIpAddress, apFtpEncryptedPassword=apFtpEncryptedPassword, ftpExtMib=ftpExtMib, apFtpStatus=apFtpStatus, apFtpEntry=apFtpEntry, apFtpTable=apFtpTable, apFtpUserName=apFtpUserName, PYSNMP_MODULE_ID=ftpExtMib, apFtpPassword=apFtpPassword)
