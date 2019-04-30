#
# PySNMP MIB module NBS-SYSLOG-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-SYSLOG-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:07:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nbs, = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, TimeTicks, ModuleIdentity, MibIdentifier, Counter32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Counter32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsSyslogServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 206))
if mibBuilder.loadTexts: nbsSyslogServerMib.setLastUpdated('200902040000Z')
if mibBuilder.loadTexts: nbsSyslogServerMib.setOrganization('NBS')
class InetAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 16))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("ipv4z", 3), ("ipv6z", 4), ("dns", 16))

nbsSyslogServerGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 206, 1))
if mibBuilder.loadTexts: nbsSyslogServerGrp.setStatus('current')
nbsSyslogServerTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 206, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyslogServerTableSize.setStatus('current')
nbsSyslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 629, 206, 1, 2), )
if mibBuilder.loadTexts: nbsSyslogServerTable.setStatus('current')
nbsSyslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1), ).setIndexNames((0, "NBS-SYSLOG-SERVER-MIB", "nbsSyslogServerIndex"))
if mibBuilder.loadTexts: nbsSyslogServerEntry.setStatus('current')
nbsSyslogServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)))
if mibBuilder.loadTexts: nbsSyslogServerIndex.setStatus('current')
nbsSyslogServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("active", 2))).clone('invalid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyslogServerStatus.setStatus('current')
nbsSyslogServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyslogServerAddressType.setStatus('current')
nbsSyslogServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyslogServerAddress.setStatus('current')
nbsSyslogServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(514)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyslogServerPort.setStatus('current')
nbsSyslogServerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("disabled", 1), ("emerg", 2), ("alert", 3), ("crit", 4), ("error", 5), ("warning", 6), ("notice", 7), ("info", 8), ("debug", 9))).clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyslogServerLevel.setStatus('current')
mibBuilder.exportSymbols("NBS-SYSLOG-SERVER-MIB", nbsSyslogServerGrp=nbsSyslogServerGrp, nbsSyslogServerPort=nbsSyslogServerPort, nbsSyslogServerTable=nbsSyslogServerTable, nbsSyslogServerIndex=nbsSyslogServerIndex, nbsSyslogServerAddressType=nbsSyslogServerAddressType, InetAddressType=InetAddressType, nbsSyslogServerTableSize=nbsSyslogServerTableSize, nbsSyslogServerLevel=nbsSyslogServerLevel, nbsSyslogServerMib=nbsSyslogServerMib, nbsSyslogServerStatus=nbsSyslogServerStatus, nbsSyslogServerAddress=nbsSyslogServerAddress, nbsSyslogServerEntry=nbsSyslogServerEntry, PYSNMP_MODULE_ID=nbsSyslogServerMib)
