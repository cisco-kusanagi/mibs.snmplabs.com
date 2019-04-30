#
# PySNMP MIB module TRAPEZE-NETWORKS-EXTERNAL-SERVER-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-EXTERNAL-SERVER-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, IpAddress, Bits, MibIdentifier, TimeTicks, iso, Unsigned32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "IpAddress", "Bits", "MibIdentifier", "TimeTicks", "iso", "Unsigned32", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzExternalServerTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 23))
trpzExternalServerTc.setRevisions(('2012-02-16 00:01',))
if mibBuilder.loadTexts: trpzExternalServerTc.setLastUpdated('201202160001Z')
if mibBuilder.loadTexts: trpzExternalServerTc.setOrganization('Trapeze Networks')
class TrpzSyslogSeverity(TextualConvention, Integer32):
    reference = 'RFC 5424, section 6.2.1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-EXTERNAL-SERVER-TC", PYSNMP_MODULE_ID=trpzExternalServerTc, TrpzSyslogSeverity=TrpzSyslogSeverity, trpzExternalServerTc=trpzExternalServerTc)
