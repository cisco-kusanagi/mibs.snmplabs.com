#
# PySNMP MIB module TPLINK-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Bits, Unsigned32, TimeTicks, Counter32, NotificationType, ObjectIdentity, MibIdentifier, Counter64, Integer32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "Unsigned32", "TimeTicks", "Counter32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter64", "Integer32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class TPRowStatus(TextualConvention, Integer32):
    description = "The status column has three defined values: - `active(1)', which indicates that the conceptual row is available for using by the managed device; - `createAndGo(4)', which is supplied by a management station wishing to create a new instance of a conceptual row and to have its status automatically set to active, making it available for using by the managed device; - `destroy(6)', which is supplied by a management station wishing to delete all of the instances associated with an existing conceptual row."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 4, 6))
    namedValues = NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6))

class TPMacAddress(TextualConvention, OctetString):
    description = "Represents an 802 MAC address represented in the `canonical' order defined by IEEE 802.1a, i.e., as if it were transmitted least significant bit first, even though 802.5 (in contrast to other 802.x protocols) requires MAC addresses to be transmitted most significant bit first."
    status = 'current'
    displayHint = '1x-1x-1x-1x-1x-1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

mibBuilder.exportSymbols("TPLINK-TC-MIB", TPMacAddress=TPMacAddress, TPRowStatus=TPRowStatus)
